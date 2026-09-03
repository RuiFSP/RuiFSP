#!/usr/bin/env python3
"""Fetch public GitHub stats nightly -> docs/data.json (no token, stdlib only).

Avoids unauthenticated rate-limit hits on every page load.
Site JS prefers ./data.json and falls back to live API.
"""
import json
import os
import urllib.request

USER = os.environ.get("GITHUB_USER", "RuiFSP")
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "data.json")

def get(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "RuiFSP-portfolio-stats",
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

def main():
    user = get(f"https://api.github.com/users/{USER}")
    repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100")
    # search API is rate-limit sensitive; tolerate failure
    try:
        prs = get(f"https://api.github.com/search/issues?q=type:pr+author:{USER}")
        prs_total = prs.get("total_count", 0)
    except Exception as e:
        print(f"prs search failed: {e}")
        prs_total = 0
    try:
        issues = get(f"https://api.github.com/search/issues?q=type:issue+author:{USER}")
        issues_total = issues.get("total_count", 0)
    except Exception as e:
        print(f"issues search failed: {e}")
        issues_total = 0

    slim_repos = [{
        "name": r.get("name"),
        "html_url": r.get("html_url"),
        "description": r.get("description"),
        "stargazers_count": r.get("stargazers_count", 0),
        "forks_count": r.get("forks_count", 0),
        "language": r.get("language"),
        "fork": r.get("fork", False),
        "pushed_at": r.get("pushed_at"),
        "size": r.get("size", 0),
    } for r in repos]

    data = {
        "user": {"login": user.get("login"), "followers": user.get("followers", 0)},
        "repos": slim_repos,
        "prs_total": prs_total,
        "issues_total": issues_total,
    }
    with open(OUT, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {OUT}: {len(slim_repos)} repos, prs={prs_total}, issues={issues_total}")

if __name__ == "__main__":
    main()
