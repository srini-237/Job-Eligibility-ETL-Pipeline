# 🚀 Automated Job Eligibility ETL Pipeline

An end-to-end data pipeline designed to automate the recruitment screening process by extracting applicant data, applying business eligibility logic, and generating actionable insights.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Architecture & Data Flow](#architecture--data-flow)
- [Technical Stack](#technical-stack)
- [ETL Logic & Transformation](#etl-logic--transformation)
- [Future Roadmap](#future-roadmap)

---

## 🎯 Project Overview
In a typical recruitment scenario, HR teams are overwhelmed with thousands of applications. This project solves that problem by implementing an automated **ETL (Extract, Transform, Load)** pipeline that shortlists candidates based on specific criteria like age and educational background.

## 🏗 Architecture & Data Flow
1. **Extract**: Data is ingested from a **MySQL** relational database containing raw applicant profiles.
2. **Transform**: A **Python/Pandas** script processes the data, validates age constraints (18+), and checks for specific degrees (B.E, B.Sc, B.Com).
3. **Load**: The "Qualified" candidates are exported into a timestamped **CSV report** for the hiring team.
4. **Orchestration**: The entire workflow is managed and scheduled by **Apache Airflow**.

## 🛠 Technical Stack
--------------------------------------------
| Category            | Technology         |
| :---                | :---               | 
| **Language**        | Python 3.x         |
| **Orchestration**   | Apache Airflow     |
| **Data Processing** | Pandas             |
| **Database**        | MySQL              |
| **Environment**     | Linux (Ubuntu/WSL) |
| **Version Control** | Git & GitHub       |
--------------------------------------------

## 🧠 ETL Logic & Transformation
Unlike basic data ingestion, this pipeline applies custom business rules:
- **Age Validation:** Filters candidates with `Age >= 18`.
- **Educational Qualification:** Matches degrees against a whitelist (`B.E`, `B.Sc`, `B.Com`).
- **Data Enrichment:** Adds a dynamic `status` column (Qualified/Not Eligible) and a `shortlist_date` for audit trails.

## 📂 Project Structure
home/ubuntu
├── airflow/dags 
│           └── applicant_etl_dag.py     # Airflow DAG definition
|
├── etl_script.py            # Core Transformation logic
│__ wrapper_script.sh        # Bash wrapper for automation
|
|
│__ extract1                 # Sample of processed data

## 📈 Future Roadmap
[ ] API Integration: Transition from local DB to live Job Board APIs.
