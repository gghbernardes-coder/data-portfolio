# Data Engineering Portfolio — gghbernardes-coder

Welcome to my data portfolio 👋  
I am a professional with **6+ years of experience in SQL (Oracle, Teradata)**, **ETL (PowerCenter)**, and data automation.  
This repository showcases practical examples of **ETL, SQL, and Python** projects that I typically deliver to freelance clients.

---

## 📂 Projects

### 1. [SQL Sales Analytics](projects/01-sql-sales-analytics)
SQL queries for sales KPIs (Oracle/Postgres/Teradata) with product ranking and query optimizations.

### 2. [ETL Customer Unification](projects/02-etl-customer-unification)
Python (pandas) pipeline that unifies CRM + ERP datasets, normalizes emails, and removes duplicates.  

#### ETL Customer Unification Example
This project demonstrates how to unify customer records from **CRM** and **ERP** sources using Python.

- **Input**:  
  - `data/crm.csv`  
  - `data/erp.csv`  
  (files with customer names, emails, and phone numbers)

- **Process**:  
  - Normalize emails (lowercase + trim).  
  - Tag source (CRM or ERP).  
  - Remove duplicates, prioritizing CRM records.  
  - Generate a single, clean dataset.

- **Output**:  
  - `outputs/unified_expected.csv` → unified and deduplicated customer base.

#### Output Example

![ETL Output](projects/02-etl-customer-unification/outputs/result.png)

### 3. [Automation Daily Report](projects/03-automation-daily-report)
Automation that generates a daily Excel report with summary and raw data tabs.  

#### Daily Report Example (Project 03)
This project automates the generation of daily reports in **Excel** from order data.

- **Input**: `data/orders.csv` (list of orders with date, status, and amount).  
- **Process**: Python script (`report.py`) reads the orders, creates a **daily summary by status** (e.g., paid, canceled, refunded), and saves it along with raw data.  
- **Output**: `outputs/daily_report.xlsx` with two tabs:
  - **Summary** → consolidated values per day/status.  
  - **Raw** → all original orders.

#### Output Example
Raw Layer

![Daily Report Excel](projects/03-automation-daily-report/outputs/camada_row.png)

Unified Summary

![Daily Report Excel](projects/03-automation-daily-report/outputs/resumo.png)

### 4. [API Enrichment (Geocoding)](projects/04-api-enrichment-geocoding)
Template to enrich addresses with latitude/longitude using APIs (Google or OpenCage).

### 5. [PowerCenter to Python Migration](projects/05-powercenter-to-python-migration)
Example of migrating transformation rules from PowerCenter to Python (pandas).

---

## 🚀 How to use
1. Open the desired project folder.  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the main script (e.g.: `python etl.py`).  
4. Results will be stored in the `outputs/` folder.

---

## 🎯 Services I offer
- Data cleaning and deduplication (CSV/Excel/SQL)  
- Optimized SQL queries (Oracle, Teradata, Postgres)  
- ETL pipelines in Python (pandas)  
- Automated reporting in Excel/CSV  

---

## 📩 Contact
- GitHub: [gghbernardes-coder](https://github.com/gghbernardes-coder)  
- LinkedIn: https://www.linkedin.com/in/gabriel-henrique-bernardes/  
- Email: yourname@example.com  
