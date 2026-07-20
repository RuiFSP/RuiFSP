#!/usr/bin/env python3
"""Generate a one-page ATS-friendly ML Engineer CV as PDF."""

from fpdf import FPDF
import os

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "docs", "Rui_Pinto_ML_Engineer_CV.pdf")


class CV(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.add_font("DJ", "", os.path.join(FONT_DIR, "DejaVuSans.ttf"), uni=True)
        self.add_font("DJ", "B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), uni=True)
        self.add_font("DJ", "I", os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf"), uni=True)
        self.add_font("DJ", "BI", os.path.join(FONT_DIR, "DejaVuSans-BoldOblique.ttf"), uni=True)
        self.set_auto_page_break(auto=True, margin=12)
        self.add_page()
        self.l_margin = 18
        self.r_margin = 18
        self.page_w = 210 - self.l_margin - self.r_margin
        self.set_margins(self.l_margin, 12, self.r_margin)

    def section_title(self, title):
        self.set_font("DJ", "B", 9.5)
        self.set_text_color(34, 34, 34)
        self.cell(self.page_w, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(34, 34, 34)
        self.line(self.l_margin, self.get_y(), 210 - self.r_margin, self.get_y())
        self.ln(2)

    def bullet(self, text, indent=4):
        self.set_x(self.l_margin + indent)
        self.set_font("DJ", "", 8)
        self.set_text_color(60, 60, 60)
        bullet_w = self.page_w - indent
        self.cell(3, 3.8, "\u2022")
        self.multi_cell(bullet_w - 3, 3.8, text)

    def body_text(self, text, bold=False, size=8):
        style = "B" if bold else ""
        self.set_font("DJ", style, size)
        self.set_text_color(60, 60, 60)
        self.multi_cell(self.page_w, 3.8, text)


cv = CV()

# ── HEADER ──
cv.set_font("DJ", "B", 16)
cv.set_text_color(20, 20, 20)
cv.cell(cv.page_w, 7, "RUI PINTO", new_x="LMARGIN", new_y="NEXT")

cv.set_font("DJ", "", 9.5)
cv.set_text_color(80, 80, 80)
cv.cell(cv.page_w, 4.5, "Data Scientist & Machine Learning Engineer", new_x="LMARGIN", new_y="NEXT")

cv.set_font("DJ", "", 7.5)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4, "Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")

cv.ln(1.5)

# Links
cv.set_font("DJ", "", 7)
cv.set_text_color(60, 120, 200)
links = "github.com/RuiFSP  |  linkedin.com/in/ruifspinto  |  ruifsp.github.io/RuiFSP"
cv.cell(cv.page_w, 4, links, new_x="LMARGIN", new_y="NEXT")
cv.set_text_color(60, 60, 60)

cv.ln(3)

# ── PROFESSIONAL SUMMARY ──
cv.section_title("Professional Summary")
cv.body_text(
    "Machine Learning Engineer with 2+ years designing and deploying production ML systems "
    "across retail, finance, public sector, and automotive. Expertise in MLOps pipelines, "
    "LLM and RAG applications, cloud-native data platforms (AWS, GCP, Azure), and forecasting "
    "at scale. Strong engineering and consulting background with a Lean Six Sigma Black Belt "
    "and MBA \u2014 bridging technical execution with business impact."
)

cv.ln(2)

# ── CORE COMPETENCIES ──
cv.section_title("Core Competencies")

skills_left = [
    "Python / SQL",
    "scikit-learn / XGBoost",
    "TensorFlow / PyTorch",
    "MLflow / Prefect",
    "Docker / Terraform",
]
skills_right = [
    "AWS SageMaker",
    "GCP (BigQuery, Spanner, ADK)",
    "Azure Databricks",
    "FastAPI / Streamlit",
    "GitHub Actions / Dagster",
]

col_w = cv.page_w / 2 - 2
for i in range(max(len(skills_left), len(skills_right))):
    cv.set_font("DJ", "", 7.5)
    cv.set_text_color(60, 60, 60)
    if i < len(skills_left):
        cv.cell(col_w, 4, "  \u2022  " + skills_left[i])
    else:
        cv.cell(col_w, 4, "")
    if i < len(skills_right):
        cv.cell(col_w, 4, "  \u2022  " + skills_right[i])
    else:
        cv.cell(col_w, 4, "")
    cv.ln(3.8)

cv.ln(1)

# ── EXPERIENCE ──
cv.section_title("Experience")

# Deloitte
cv.set_font("DJ", "B", 8.5)
cv.set_text_color(34, 34, 34)
cv.cell(cv.page_w, 4.5, "Deloitte  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("DJ", "I", 7.5)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4, "Tech Senior / Tech Consultant, AI & Data  |  Dec 2024 \u2013 Present", new_x="LMARGIN", new_y="NEXT")
cv.ln(1)

deloitte_bullets = [
    "Built ML forecasting models for project expenditure tracking using AWS SageMaker, integrating real-time financial data to improve budget accuracy",
    "Designed and deployed a RAG agent using Google ADK, Cloud Spanner, and BigQuery for enterprise-scale intelligent retrieval and contextual reasoning",
    "Developed AI forecasting tools using Model Context Protocol (MCP), integrated with SAP systems via AWS SageMaker",
    "Built sales forecasting models for a retail client using Temporal Fusion Transformers on Azure Databricks for demand planning and anomaly detection",
    "Led data anonymization for a public sector tax program using NER models on GCP to protect sensitive data while maintaining analytical value",
    "Orchestrated ETL pipelines with Dagster in the automotive sector, integrating front-end and back-end systems",
]
for b in deloitte_bullets:
    cv.bullet(b)
cv.ln(2)

# Le Wagon
cv.set_font("DJ", "B", 8.5)
cv.set_text_color(34, 34, 34)
cv.cell(cv.page_w, 4.5, "Le Wagon  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("DJ", "I", 7.5)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4, "Data Science Instructor & Batch Manager  |  Jan 2024 \u2013 Dec 2024", new_x="LMARGIN", new_y="NEXT")
cv.ln(1)

lewagon_bullets = [
    "Taught Data Science and Data Analytics bootcamps, mentoring students through end-to-end ML projects from EDA to deployment",
    "Managed cohort operations, project supervision, and Demo Day presentations across 7 cohorts",
]
for b in lewagon_bullets:
    cv.bullet(b)

cv.ln(2)

# ── FEATURED PROJECTS ──
cv.section_title("Featured Projects")

projects = [
    ("MLOps Pipeline (Premier League Prediction)",
     "MLflow, FastAPI, Prefect, PostgreSQL, Grafana, Docker \u2014 github.com/RuiFSP/mlops-2025-final_project"),
    ("Bike Demand Forecasting",
     "Kedro, CatBoost, Dash, Docker Compose \u2014 github.com/RuiFSP/kedro-bike-demand-pipeline"),
    ("DE Data Platform",
     "GCP (Terraform, BigQuery, Cloud Run), Streamlit \u2014 github.com/RuiFSP/dezoomcamp-2026-final-project"),
]
for title, desc in projects:
    cv.set_font("DJ", "B", 7.5)
    cv.set_text_color(34, 34, 34)
    cv.cell(3, 3.8, "\u2022")
    cv.cell(60, 3.8, title)
    cv.set_font("DJ", "", 7)
    cv.set_text_color(100, 100, 100)
    cv.multi_cell(cv.page_w - 63, 3.8, desc)

cv.ln(2)

# ── EDUCATION ──
cv.section_title("Education")

edu = [
    ("Data Science & AI Bootcamp", "Le Wagon, 2023"),
    ("Full Stack Developer Bootcamp", "Code for All_, 2022"),
    ("MBA, Business Administration", "ISEG, 2013"),
    ("Lean Six Sigma Black Belt", "ASQ, 2014"),
    ("MSc, Mechanical Engineering", "Instituto Superior Tecnico, 2007"),
]
for title, detail in edu:
    cv.set_font("DJ", "B", 8)
    cv.set_text_color(34, 34, 34)
    cv.cell(3, 4, "\u2022")
    cv.cell(62, 4, title)
    cv.set_font("DJ", "", 7.5)
    cv.set_text_color(100, 100, 100)
    cv.cell(cv.page_w - 65, 4, detail, new_x="LMARGIN", new_y="NEXT")
    cv.ln(0.5)

cv.ln(4)
cv.set_font("DJ", "I", 6.5)
cv.set_text_color(150, 150, 150)
cv.cell(cv.page_w, 4, "Full career history available on LinkedIn", align="C", new_x="LMARGIN", new_y="NEXT")

cv.output(OUTPUT)
print(f"PDF generated: {OUTPUT}")
