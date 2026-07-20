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
        self.cell(self.page_w, 5.5, title.upper(), new_x="LMARGIN", new_y="NEXT")
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
cv.cell(cv.page_w, 5, "Data Scientist & Machine Learning Engineer", new_x="LMARGIN", new_y="NEXT")

cv.set_font("Helvetica", "", 8)
cv.set_text_color(110, 110, 110)
cv.cell(cv.page_w, 4.5, "Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")

cv.ln(1.5)

cv.set_font("Helvetica", "", 7.5)
cv.set_text_color(50, 110, 200)
links = "github.com/RuiFSP  |  linkedin.com/in/ruifspinto  |  ruifsp.github.io/RuiFSP"
cv.cell(cv.page_w, 4.5, links, new_x="LMARGIN", new_y="NEXT")
cv.set_text_color(60, 60, 60)

cv.ln(3.5)

# -- PROFESSIONAL SUMMARY --
cv.section_title("Professional Summary")
cv.body_text(
    "Machine Learning Engineer with 2+ years designing and deploying production ML systems "
    "across retail, finance, public sector, and automotive. Expertise in MLOps pipelines, "
    "LLM and RAG applications, cloud-native data platforms (AWS, GCP, Azure), and forecasting "
    "at scale. Strong engineering and consulting background with a Lean Six Sigma Black Belt "
    "and MBA - bridging technical execution with business impact."
)

cv.ln(3)

# -- CORE COMPETENCIES --
cv.section_title("Core Competencies")

competencies = [
    "Python, SQL, scikit-learn, XGBoost, TensorFlow, PyTorch",
    "MLflow, Prefect, Dagster, Docker, Terraform, GitHub Actions",
    "AWS SageMaker, GCP (BigQuery, Spanner, ADK), Azure Databricks",
    "FastAPI, Streamlit, Kedro, Airflow",
]
for comp in competencies:
    cv.set_font("Helvetica", "", 8.5)
    cv.set_text_color(60, 60, 60)
    cv.cell(3.5, 4.5, "-")
    cv.cell(cv.page_w - 3.5, 4.5, comp, new_x="LMARGIN", new_y="NEXT")

cv.ln(2.5)

# -- EXPERIENCE --
cv.section_title("Experience")

# Deloitte
cv.set_font("Helvetica", "B", 9)
cv.set_text_color(33, 33, 33)
cv.cell(cv.page_w, 5, "Deloitte  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("Helvetica", "I", 8)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4.5, "Tech Senior / Tech Consultant, AI & Data  |  Dec 2024 - Present", new_x="LMARGIN", new_y="NEXT")
cv.ln(1.5)

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
cv.ln(2.5)

# Le Wagon
cv.set_font("Helvetica", "B", 9)
cv.set_text_color(33, 33, 33)
cv.cell(cv.page_w, 5, "Le Wagon  |  Lisbon, Portugal", new_x="LMARGIN", new_y="NEXT")
cv.set_font("Helvetica", "I", 8)
cv.set_text_color(100, 100, 100)
cv.cell(cv.page_w, 4.5, "Data Science Instructor & Batch Manager  |  Jan 2024 - Dec 2024", new_x="LMARGIN", new_y="NEXT")
cv.ln(1.5)

lewagon_bullets = [
    "Taught Data Science and Data Analytics bootcamps, mentoring students through end-to-end ML projects from EDA to deployment",
    "Managed cohort operations, project supervision, and Demo Day presentations across 7 cohorts",
]
for b in lewagon_bullets:
    cv.bullet(b)

cv.ln(2.5)

# -- FEATURED PROJECTS --
cv.section_title("Featured Projects")

projects = [
    ("MLOps Pipeline (Premier League Prediction)",
     "MLflow, FastAPI, Prefect, PostgreSQL, Grafana, Docker - github.com/RuiFSP/mlops-2025-final_project"),
    ("Bike Demand Forecasting",
     "Kedro, CatBoost, Dash, Docker Compose - github.com/RuiFSP/kedro-bike-demand-pipeline"),
    ("DE Data Platform",
     "GCP (Terraform, BigQuery, Cloud Run), Streamlit - github.com/RuiFSP/dezoomcamp-2026-final-project"),
]
for title, desc in projects:
    cv.set_font("Helvetica", "B", 8.5)
    cv.set_text_color(33, 33, 33)
    cv.cell(3.5, 4.5, "-")
    cv.cell(65, 4.5, title)
    cv.set_font("Helvetica", "", 8)
    cv.set_text_color(100, 100, 100)
    cv.multi_cell(cv.page_w - 68.5, 4.5, desc)

cv.ln(1.5)

# -- EDUCATION --
cv.section_title("Education")

edu = [
    ("Data Science & AI Bootcamp", "Le Wagon, 2023"),
    ("Full Stack Developer Bootcamp", "Code for All_, 2022"),
    ("MBA, Business Administration", "ISEG, 2013"),
    ("Lean Six Sigma Black Belt", "ASQ, 2014"),
    ("MSc, Mechanical Engineering", "Instituto Superior Tecnico, 2007"),
]
for title, detail in edu:
    cv.set_font("Helvetica", "B", 8.5)
    cv.set_text_color(33, 33, 33)
    cv.cell(3.5, 4.5, "-")
    cv.cell(65, 4.5, title)
    cv.set_font("Helvetica", "", 8)
    cv.set_text_color(100, 100, 100)
    cv.cell(cv.page_w - 68.5, 4.5, detail, new_x="LMARGIN", new_y="NEXT")

cv.ln(3)
cv.set_font("Helvetica", "I", 7)
cv.set_text_color(160, 160, 160)
cv.cell(cv.page_w, 4, "Full career history available on LinkedIn", align="C", new_x="LMARGIN", new_y="NEXT")

cv.output(OUTPUT)
print(f"PDF generated: {OUTPUT}")
