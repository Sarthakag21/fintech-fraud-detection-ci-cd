# 🚀 FinTech Fraud Detection Pipeline – CI/CD Extension

> **Extension Project**  
> This repository extends the original **FinTech Fraud Detection Pipeline** by implementing modern **DevOps** and **CI/CD** practices for Azure Databricks. The focus of this project is to automate deployment of Databricks jobs and notebooks using **Databricks Asset Bundles** and **GitHub Actions**, eliminating manual deployments and enabling Infrastructure as Code (IaC).

---

## 📌 Background

The original project implemented a real-time fraud detection pipeline on Azure using:

- Azure Event Hub
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks (PySpark Structured Streaming)
- Delta Lake (Bronze → Silver → Gold)
- Streamlit Dashboard
- Power BI Dashboard

While the data pipeline was fully functional, deployment of notebooks and jobs was manual.

This extension automates the deployment process following modern Data Engineering DevOps practices.

---

# 🎯 Objectives

This project introduces:

- Databricks Asset Bundles (DAB)
- Infrastructure as Code (IaC)
- GitHub Actions CI/CD
- Automated Job Deployment
- Version Controlled Databricks Resources
- Automated Bundle Validation
- Repeatable Deployments

---

# 🏗 Existing Data Pipeline

```
               Azure Event Hub
                      │
                      ▼
           Azure Data Factory
                      │
                      ▼
             ADLS Gen2 (Landing)
                      │
                      ▼
         Azure Databricks Streaming
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     Bronze        Silver        Gold
                      │
                      ▼
              Fraud Detection
                      │
                      ▼
          Dashboard Export (CSV)
                      │
                      ▼
      Streamlit Dashboard / Power BI
```

---

# 🚀 CI/CD Architecture

```
          Developer
              │
        Git Commit
              │
        Git Push
              │
              ▼
      GitHub Repository
              │
              ▼
      GitHub Actions Workflow
              │
      ┌───────────────┐
      │ Bundle Validate│
      └───────────────┘
              │
              ▼
       Bundle Deploy
              │
              ▼
     Azure Databricks Workspace
              │
      ┌──────────────┐
      │ Bronze Job   │
      │ Silver Job   │
      │ Gold Job     │
      │ Dashboard Job│
      └──────────────┘
```

---

# 🏗 Project Structure

```
fintech-fraud-detection-cicd
│
├── .github/
│   └── workflows/
│       └── databricks-ci.yml
│
├── resources/
│   ├── bronze.job.yml
│   ├── silver.job.yml
│   ├── gold.job.yml
│   └── dashboard.job.yml
│
├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── dashboard/
│   └── data_generator/
│
├── tests/
├── fixtures/
│
├── databricks.yml
├── pyproject.toml
└── README.md
```

---

# ⚙ Technologies Used

| Category | Technologies |
|-----------|-------------|
| Cloud | Microsoft Azure |
| Data Engineering | Azure Databricks |
| Language | Python |
| Processing | PySpark |
| Storage | ADLS Gen2 |
| Streaming | Azure Event Hub |
| ETL | Azure Data Factory |
| Lakehouse | Delta Lake |
| CI/CD | GitHub Actions |
| IaC | Databricks Asset Bundles |
| Version Control | Git |
| Dashboard | Streamlit, Power BI |

---

# 🔄 CI/CD Workflow

Whenever code is pushed to GitHub:

```
Push
   │
   ▼
Checkout Repository
   │
   ▼
Setup Python
   │
   ▼
Install Databricks CLI
   │
   ▼
Bundle Validation
   │
   ▼
Bundle Deployment
   │
   ▼
Azure Databricks
```

This ensures every deployment is validated and reproducible.

---

# ✨ Features

- Automated Databricks Job Deployment
- Infrastructure as Code
- Version Controlled Workspace
- Automatic Bundle Validation
- Multi-job Deployment
- GitHub Actions Integration
- Repeatable Deployments
- Zero Manual Notebook Uploads

---

# 🎯 Business Benefits

- Eliminates manual deployment errors
- Faster deployment cycles
- Consistent Databricks environments
- Improved collaboration
- Version-controlled infrastructure
- Easy rollback using Git history
- Reproducible deployments

---

# 📊 Achievements

✅ Converted manual Databricks deployment into Infrastructure as Code.

✅ Automated deployment of Bronze, Silver, Gold and Dashboard jobs.

✅ Implemented GitHub Actions pipeline for validation and deployment.

✅ Used Databricks Asset Bundles for resource management.

✅ Enabled automated deployment directly from GitHub.

---

# 📸 Screenshots

- GitHub Actions successful workflow
- Bundle validation
- Bundle deployment
- Databricks Jobs
- Repository Structure
- Architecture Diagram

---

# 🚀 Future Improvements

- Production Deployment Target
- Terraform Integration
- Azure Key Vault Secrets
- Service Principal Authentication
- Unit Testing for PySpark
- Slack/Teams Deployment Notifications
- Multi-environment Deployment (Dev/Test/Prod)

---

# 👨‍💻 Author

**Sarthak Agarwal**

Data Engineer | Azure | Databricks | PySpark | Delta Lake | CI/CD | GitHub Actions

---

## 🔗 Related Project

This repository is an extension of the **Real-Time FinTech Fraud Detection Pipeline**, focusing specifically on deployment automation and Infrastructure as Code for Azure Databricks.
