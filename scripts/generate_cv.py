#!/usr/bin/env python3
"""Generate an ATS-optimized one-page ML Engineer CV as PDF."""

from fpdf import FPDF
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "docs", "Rui_Pinto_ML_Engineer_CV.pdf")


class CV(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.set_auto_page_break(auto=True, margin=10)
        self.add_page()
        self.l_margin = 15
        self.r_margin = 15
        self.page_w = 210 - self.l_margin - self.r_margin
        self.set_margins(self.l_margin, 10, self.r_margin)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(33, 33, 33)
        self.cell(self.page_w, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(33, 33, 33)
        self.line(self.l_margin, self.get_y(), 210 - self.r_margin, self.get_y())
        self.ln(2)

    def bullet(self, text, indent=3):
        self.set_x(self.l_margin + indent)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(60, 60, 60)
        bw = self.page_w - indent
        self.cell(3.5, 4.5, "-")
        self.multi_cell(bw - 3.5, 4.5, text)

    def body_text(self, text, bold=False, size=9):
        style = "B" if bold else ""
        self.set_font("Helvetica", style, size)
        self.set_text_color(60, 60, 60)
        self.multi_cell(self.page_w, 4.5, text)


cv = CV()

# -- HEADER --
cv.set_font("Helvetica", "B", 20)
cv.set_text_color(18, 18, 18)
cv.cell(cv.page_w, 8, "RUI PINTO", new_x="LMARGIN", new_y="NEXT")

cv.set_font("Helvetica", "", 10)
cv.set_text_color(80, 80, 80)
cv.cell(cv.page_w, 5.5, "Data Scientist & Machine Learning Engineer", new_x="LMARGIN", new_y="NEXT")

cv.set_font("Helvetica", "", 8)
cv.set_text_color(110, 110, 110)
cv.cell(cv.page_w, 5, "Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")

cv.ln(2)

cv.set_font("Helvetica", "", 7.5)
cv.set_text_color(50, 110, 200)
cv.cell(38, 5, "github.com/RuiFSP", link="https://github.com/RuiFSP")
cv.set_text_color(150, 150, 150)
cv.cell(6, 5, "|")
cv.set_text_color(50, 110, 200)
cv.cell(50, 5, "linkedin.com/in/ruifspinto", link="https://linkedin.com/in/ruifspinto")
cv.set_text_color(150, 150, 150)
cv.cell(6, 5, "|")
cv.set_text_color(50, 110, 200)
cv.cell(cv.page_w - 100, 5, "ruifsp.github.io/RuiFSP", link="https://ruifsp.github.io/RuiFSP", new_x="LMARGIN", new_y="NEXT")
cv.set_text_color(60, 60, 60)

cv.ln(3.5)

# -- PROFESSIONAL SUMMARY --
cv.section_title("Professional Summary")
cv.body_text(
    "Machine Learning Engineer delivering production ML systems across retail, finance, "
    "public sector, and automotive. End-to-end expertise from data pipelines and forecasting "
    "models to LLM/RAG applications and MLOps deployment on AWS, GCP, and Azure. MBA and "
    "Lean Six Sigma Black Belt - translating technical execution into business outcomes."
)

cv.ln(3.5)

# -- CORE COMPETENCIES --
cv.section_title("Core Competencies")

competencies = [
    "ML Engineering: Python, scikit-learn, XGBoost, TensorFlow, PyTorch, FastAPI, Streamlit",
    "MLOps & Pipelines: MLflow, Prefect, Dagster, Docker, Terraform, GitHub Actions, Kedro",
    "Cloud & Data: AWS SageMaker, GCP (BigQuery, Spanner, ADK, Cloud Run), Azure Databricks",
    "LLMs & AI: RAG pipelines, Google ADK, LangChain, NER, MCP, Temporal Fusion Transformers",
]
for comp in competencies:
    cv.set_font("Helvetica", "", 8.5)
    cv.set_text_color(60, 60, 60)
    cv.cell(3.5, 4.5, "-")
    cv.cell(cv.page_w - 3.5, 4.5, comp, new_x="LMARGIN", new_y="NEXT")

cv.ln(1.5)

# -- EXPERIENCE --
cv.section_title("Experience")

# Deloitte
cv.set_font("Helvetica", "B", 9)
cv.set_text_color(33, 33, 33)
cv.cell(cv.page_w, 4.5, "Deloitte  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("Helvetica", "I", 8)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4.5, "Tech Senior / Tech Consultant, AI & Data  |  Dec 2024 - Present", new_x="LMARGIN", new_y="NEXT")
cv.ln(1.5)

deloitte_bullets = [
    "Built ML forecasting models on AWS SageMaker integrating real-time financial data, improving budget accuracy for project expenditure tracking",
    "Designed and deployed a RAG agent using Google ADK, Cloud Spanner, and BigQuery for enterprise-scale intelligent document retrieval and analytics",
    "Developed AI forecasting tools via Model Context Protocol (MCP), integrated with SAP systems on AWS SageMaker",
    "Built retail demand forecasting with Temporal Fusion Transformers on Azure Databricks, enabling anomaly detection and improving planning accuracy",
    "Applied NER models on GCP for large-scale data anonymization in a public sector tax program, balancing data protection with analytical value",
    "Orchestrated ETL pipelines with Dagster in the automotive sector, integrating cross-system data flows for automated reporting",
]
for b in deloitte_bullets:
    cv.bullet(b)
cv.ln(2)

# Le Wagon
cv.set_font("Helvetica", "B", 9)
cv.set_text_color(33, 33, 33)
cv.cell(cv.page_w, 4.5, "Le Wagon  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("Helvetica", "I", 8)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4.5, "Data Science Instructor & Batch Manager  |  Jan 2024 - Dec 2024", new_x="LMARGIN", new_y="NEXT")
cv.ln(1.5)

lewagon_bullets = [
    "Taught Data Science and Data Analytics across 7 cohorts, guiding end-to-end ML projects from EDA to deployment",
    "Managed cohort operations, project supervision, and Demo Day presentations",
]
for b in lewagon_bullets:
    cv.bullet(b)

cv.ln(2)

# Earlier Career
cv.set_font("Helvetica", "B", 9)
cv.set_text_color(33, 33, 33)
cv.cell(cv.page_w, 4.5, "Earlier Career", new_x="LMARGIN", new_y="NEXT")
cv.ln(1)
cv.set_font("Helvetica", "", 8)
cv.set_text_color(100, 100, 100)
cv.multi_cell(cv.page_w, 4.2,
    "Java Developer @ BNP Paribas (global booking & allocation)  |  "
    "Lean Six Sigma Black Belt, Sigma4Profit founder  |  "
    "Operations & Quality Management across industries  |  "
    "Mechanical Engineering R&D, IST"
)

cv.ln(2.5)

# -- FEATURED PROJECTS --
cv.section_title("Featured Projects")

projects = [
    ("LLM RAG Pipeline (Portuguese Food & Wine Guide)",
     "Qdrant, Flask, PostgreSQL, Grafana, GPT-4o, Docker Compose",
     "https://github.com/RuiFSP/llmzoomcamp-2026-final-project"),
    ("Data Engineering Platform (GitHub Analytics)",
     "Terraform, GCS, BigQuery, Bruin, Streamlit, Cloud Run, CI/CD",
     "https://github.com/RuiFSP/dezoomcamp-2026-final-project"),
    ("MLOps Pipeline (Premier League Prediction, 61.8% accuracy)",
     "FastAPI, MLflow, Prefect, PostgreSQL, Grafana, Docker, GitHub Actions",
     "https://github.com/RuiFSP/mlops-2025-final_project"),
]
for title, stack, url in projects:
    cv.set_font("Helvetica", "B", 9)
    cv.set_text_color(33, 33, 33)
    cv.cell(cv.page_w, 4.5, title, new_x="LMARGIN", new_y="NEXT")
    cv.set_font("Helvetica", "I", 8)
    cv.set_text_color(100, 100, 100)
    cv.cell(cv.page_w, 4.5, stack, new_x="LMARGIN", new_y="NEXT", link=url)
    cv.ln(1)

cv.ln(1.5)

# -- EDUCATION --
cv.section_title("Education")

edu = [
    ("Data Science & AI Bootcamp", "Le Wagon, 2023"),
    ("Full Stack Developer Bootcamp", "Code for All_, 2022"),
    ("MBA, Business Administration", "ISEG, 2013"),
    ("Lean Six Sigma Black Belt", "ASQ, 2014"),
    ("MSc, Mechanical Engineering", "Instituto Superior Tecnico (IST), 2007"),
]
for title, detail in edu:
    cv.set_font("Helvetica", "B", 8.5)
    cv.set_text_color(33, 33, 33)
    cv.cell(3.5, 5, "-")
    cv.cell(62, 5, title)
    cv.set_font("Helvetica", "", 8)
    cv.set_text_color(100, 100, 100)
    cv.cell(cv.page_w - 65.5, 5, detail, new_x="LMARGIN", new_y="NEXT")

cv.ln(2.5)
cv.set_draw_color(180, 180, 180)
cv.line(cv.l_margin, cv.get_y(), 210 - cv.r_margin, cv.get_y())
cv.ln(2.5)
cv.set_font("Helvetica", "", 7.5)
cv.set_text_color(120, 120, 120)
cv.cell(cv.page_w, 4, "Languages: Portuguese (native)  |  English (full professional)", new_x="LMARGIN", new_y="NEXT")

cv.output(OUTPUT)
print(f"PDF generated: {OUTPUT}")
