# Payment & Fraud Analytics Platform

An end-to-end cloud-based data analytics platform built on AWS that transforms raw payment transaction data into actionable business insights through ETL pipelines, SQL analytics, and interactive Power BI dashboards.

---

## Project Overview

Modern payment platforms process millions of transactions daily, making it increasingly difficult for organizations to monitor business performance, detect fraud patterns, and understand customer and merchant behaviour.

This project demonstrates how cloud-based data engineering and business intelligence can be combined to build a scalable analytics solution capable of supporting executive reporting and operational decision-making.

The solution leverages AWS services for data ingestion, validation, transformation, and querying before presenting business insights through interactive Power BI dashboards.

---

# Business Problem

Financial organizations require timely insights into transaction activity to answer questions such as:

- How is the business performing over time?
- Which merchant categories generate the highest revenue?
- Which regions contribute the most business?
- Where is fraudulent activity concentrated?
- How do customer spending patterns change throughout the day?
- Which customer segments generate the highest value?

Raw transactional datasets alone cannot answer these questions effectively. A structured analytics platform is required to transform raw payment records into business-ready datasets suitable for reporting and decision making.

---

# Solution Architecture

The platform follows a modern cloud analytics architecture.

```
                    Raw Payment Dataset
                           │
                           ▼
                 Amazon S3 (Raw Zone)
                           │
                           ▼
                AWS Lambda Validation
                           │
                           ▼
               AWS Glue Visual ETL Job
                           │
                           ▼
              Amazon S3 (Curated Parquet)
                           │
                           ▼
                 AWS Glue Data Catalog
                           │
                           ▼
                    Amazon Athena
                           │
                           ▼
                 SQL Analytical Views
                           │
                           ▼
                    Microsoft Power BI
```

---

# AWS Data Pipeline

## 1. Amazon S3

Acts as the centralized data lake.

Folders:

- `raw/`
- `curated/`
- `config/`

---

## 2. AWS Lambda

A validation function checks incoming datasets before processing.

Validation includes:

- Schema verification
- Column validation
- File integrity checks

This ensures only valid datasets proceed into the ETL pipeline.

---

## 3. AWS Glue Visual ETL

AWS Glue transforms the raw CSV dataset into an optimized analytics dataset.

Transformations performed include:

- Data type conversion
- Column standardization
- Removal of unnecessary attributes
- Creation of curated Parquet files
- Performance optimization for analytical queries

---

## 4. AWS Glue Data Catalog

Automatically catalogs curated datasets, allowing Athena to query them without requiring manual schema creation.

---

## 5. Amazon Athena

Athena performs SQL analytics directly on curated Parquet files stored in Amazon S3.

Instead of querying raw transactional data repeatedly, analytical SQL views were created for reporting.

---

# Data Warehouse Design

The analytical layer was designed using a dimensional modeling approach.

### Fact Table

**Fact Transactions**

Contains transactional measures including:

- Transaction Amount
- Fraud Indicator
- Transaction Timestamp

---

### Dimensions

- Date Dimension
- Merchant Dimension
- Customer Dimension
- Geography Dimension

This design enables efficient analytical queries while maintaining scalability for future enhancements.

---

# SQL Analysis

Rather than connecting Power BI directly to transactional data, SQL views were created in Amazon Athena to answer specific business questions.

## Analytical Views

### `vw_transaction_summary`

Provides executive-level KPIs including:

- Revenue
- Transaction Volume
- Fraud Rate
- Monthly Trends

---

### `vw_merchant_analysis`

Supports merchant reporting by providing:

- Revenue by Merchant
- Revenue by Category
- Fraud Metrics
- Transaction Volume

---

### `vw_geographic_analysis`

Provides regional insights including:

- Revenue by State
- Revenue by City
- Fraud Rate by Region
- Transaction Distribution

---

### `vw_customer_activity`

Analyzes customer behaviour including:

- Spending Patterns
- Occupation Analysis
- Transaction Hour
- Fraud Activity

These SQL views simplify Power BI development while improving report performance and maintainability.

---

# Power BI Dashboard Analysis

The reporting layer consists of three interactive dashboards designed for different business stakeholders.

---

## Executive Dashboard

### Purpose

Provide executives with a high-level overview of business performance.

### Business Questions

- How much revenue has the platform generated?
- How many transactions have been processed?
- Is fraud increasing?
- Which states contribute the highest revenue?
- How are revenue and transaction volumes changing over time?

### Key Visuals

- KPI Cards
- Monthly Revenue Trend
- Monthly Transaction Trend
- Monthly Fraud Trend
- Revenue by State Map
- Transaction Volume by State
- Fraud Rate by State

---

## Merchant Analytics

### Purpose

Analyze merchant performance while balancing commercial value with fraud exposure.

### Business Questions

- Which merchant categories generate the most revenue?
- Which merchant categories contribute the most fraud?
- Which merchants generate the highest revenue?
- How does transaction volume compare with revenue?
- Which merchants require additional fraud monitoring?

### Key Visuals

- Top Revenue Categories
- Top Fraud Categories
- Transaction Volume vs Revenue
- Top Merchant Revenue & Fraud Comparison
- Merchant Performance Table

---

## Customer Analytics

### Purpose

Understand customer behaviour and transaction patterns.

### Business Questions

- When are customers most active?
- Which hours generate the highest revenue?
- When is fraud most likely to occur?
- Which occupations contribute the highest spending?
- How does spending vary across occupations and gender?

### Key Visuals

- Hourly Transaction Trend
- Hourly Revenue Trend
- Hourly Fraud Trend
- Top Fraud-Contributing Occupations
- Spending by Occupation & Gender

---

# Key Business Insights

The analytics platform enables organizations to:

- Monitor overall payment platform performance through executive KPIs.
- Identify revenue growth trends and seasonal transaction patterns.
- Detect fraud concentration across merchant categories and geographic regions.
- Compare merchant performance using both revenue and fraud metrics.
- Understand customer transaction behaviour throughout the day.
- Identify customer segments with higher spending potential.
- Support operational and strategic decision-making through interactive dashboards.

---

# Tech Stack

## Cloud Services

- Amazon S3
- AWS Lambda
- AWS Glue
- AWS Glue Data Catalog
- Amazon Athena
- AWS IAM

## Data Engineering

- SQL
- AWS Glue Visual ETL
- Parquet
- Data Warehouse Modeling

## Business Intelligence

- Microsoft Power BI
- DAX
- Power Query

## Programming

- Python
- Pandas

---

## Author

**Aakash D**

Data Analyst | AWS Certified Solutions Architect – Associate | Leveraging Data to solve Business problems