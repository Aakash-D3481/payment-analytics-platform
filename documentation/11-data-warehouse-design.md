# Data Warehouse Design

## Project

Payment Analytics Platform

---

# 1. Business Problem

Financial institutions process millions of payment transactions every day across thousands of merchants and customers.

The raw transaction data is highly denormalized and optimized for operational processing rather than analytical reporting.

As a result:

- Reporting queries become inefficient.
- Business metrics are difficult to calculate consistently.
- Time-based analysis requires repeated transformations.
- Customer and merchant information is duplicated across every transaction.

The objective of this project is to build a cloud-based analytics platform that transforms raw transaction data into a reporting-ready dimensional model using AWS Glue.

The curated data will support executive reporting, fraud analysis, merchant performance analysis, and customer analytics through Amazon Athena and Power BI.

---

# 2. Business Objectives

The platform should enable stakeholders to answer questions such as:

## Executive Leadership

- How many payment transactions were processed?
- What is the total payment value?
- What percentage of transactions are fraudulent?
- What is the total fraud loss?
- How are transaction volumes changing over time?
- Which states generate the highest payment volume?

---

## Fraud Analytics Team

- Which merchant categories have the highest fraud rate?
- Which merchants experience the highest fraud losses?
- Which hours of the day experience the most fraud?
- Which customer demographics are most affected?
- Which occupations experience higher fraud exposure?

---

## Merchant Operations

- Top merchants by transaction value
- Top merchants by transaction count
- Merchant category performance
- Geographic merchant distribution

---

## Customer Analytics

- Customer spending behaviour
- Average transaction value
- Spending by age group
- Spending by occupation
- Spending by gender
- Geographic spending distribution

---

# 3. KPI Catalogue

| KPI | Business Definition |
|------|---------------------|
| Total Transactions | Number of processed payment transactions |
| Total Transaction Value | Sum of all transaction amounts |
| Average Transaction Value | Average transaction amount |
| Fraud Transactions | Count of fraudulent transactions |
| Fraud Rate | Fraud Transactions / Total Transactions |
| Fraud Loss | Sum of fraudulent transaction amounts |
| Active Customers | Distinct customers making transactions |
| Active Merchants | Distinct merchants processing transactions |
| Average Spend per Customer | Total Spend / Distinct Customers |
| Average Spend per Merchant | Total Spend / Distinct Merchants |

---

# 4. Dimensional Model

The warehouse follows a Star Schema optimized for analytical reporting.

Fact Table

- Fact_Transactions

Dimension Tables

- Dim_Customer
- Dim_Merchant
- Dim_Date
- Dim_Location

---

# 5. Star Schema

```

```
                 Dim_Date
                     │
                     │
Dim_Customer ─ Fact_Transactions ─ Dim_Merchant
                     │
                     │
               Dim_Location
```

```

---

# 6. Fact Table

## Fact_Transactions

| Column |
|---------|
| Transaction_ID |
| Customer_Key |
| Merchant_Key |
| Date_Key |
| Location_Key |
| Transaction_Amount |
| Fraud_Flag |

Measures

- Transaction Amount
- Fraud Flag

---

# 7. Dimension Tables

## Dim_Customer

| Column |
|---------|
| Customer_Key |
| Credit_Card_Number |
| Full_Name |
| Gender |
| Date_of_Birth |
| Customer_Age |
| Occupation |

---

## Dim_Merchant

| Column |
|---------|
| Merchant_Key |
| Merchant_Name |
| Merchant_Category |
| Merchant_Latitude |
| Merchant_Longitude |

---

## Dim_Location

| Column |
|---------|
| Location_Key |
| City |
| State |
| ZIP |
| Latitude |
| Longitude |
| Population |

---

## Dim_Date

| Column |
|---------|
| Date_Key |
| Transaction_Date |
| Year |
| Quarter |
| Month |
| Month_Name |
| Week |
| Day |
| Day_Name |
| Hour |
| Weekend_Flag |

---

# 8. Raw to Target Mapping

| Raw Column | Target Table |
|------------|--------------|
| trans_num | Fact_Transactions |
| amt | Fact_Transactions |
| is_fraud | Fact_Transactions |
| trans_date_trans_time | Fact_Transactions + Dim_Date |
| cc_num | Dim_Customer |
| first | Dim_Customer |
| last | Dim_Customer |
| gender | Dim_Customer |
| dob | Dim_Customer |
| job | Dim_Customer |
| merchant | Dim_Merchant |
| category | Dim_Merchant |
| merch_lat | Dim_Merchant |
| merch_long | Dim_Merchant |
| city | Dim_Location |
| state | Dim_Location |
| zip | Dim_Location |
| lat | Dim_Location |
| long | Dim_Location |
| city_pop | Dim_Location |

---

# 9. ETL Transformation Rules

AWS Glue performs the following transformations:

- Convert timestamp columns to datetime.
- Convert date of birth to date datatype.
- Remove duplicate records.
- Standardize column names.
- Generate surrogate keys for dimensions.
- Create dimensional tables.
- Create fact table.
- Export optimized Parquet datasets.

---

# 10. Derived Columns

| Derived Column | Description |
|----------------|-------------|
| Customer_Age | Calculated from DOB |
| Transaction_Date | Extracted from timestamp |
| Transaction_Year | Derived from timestamp |
| Transaction_Quarter | Derived from timestamp |
| Transaction_Month | Derived from timestamp |
| Month_Name | Derived from timestamp |
| Day_Name | Derived from timestamp |
| Transaction_Hour | Derived from timestamp |
| Weekend_Flag | Saturday/Sunday indicator |

---

# 11. Curated Data Lake Structure

```

```
curated/

    fact_transactions/

    dim_customer/

    dim_merchant/

    dim_date/

    dim_location/
```

```

All curated datasets will be stored as Apache Parquet files.

---

# 12. Why a Star Schema?

The dimensional model provides:

- Faster analytical queries
- Simplified dashboard development
- Reduced data duplication
- Improved maintainability
- Better scalability for future reporting requirements

---

# 13. Downstream Consumers

AWS Glue

↓

AWS Glue Data Catalog

↓

Amazon Athena

↓

Power BI

All business reporting will consume only the curated star schema rather than the raw transactional dataset.