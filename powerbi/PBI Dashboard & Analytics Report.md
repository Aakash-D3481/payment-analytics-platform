# Power BI Dashboard Analysis

## Dashboard Overview

The Payment & Fraud Analytics dashboard was developed to transform transaction-level payment data into actionable business insights. The dashboard is divided into three reporting layers, each designed for a different business audience.

- **Executive View** – Overall business performance and fraud monitoring.
- **Merchant Analytics** – Merchant category performance and fraud analysis.
- **Customer Analytics** – Customer spending behaviour and transaction patterns.

The reports are powered by curated datasets stored in Amazon S3, processed using AWS Glue ETL, queried through Amazon Athena, and visualized using Microsoft Power BI.

---

screenshots/Executive View.png

# Executive View

## Objective

Provide executives with a high-level overview of payment activity, revenue generation, and fraud performance.

This page answers questions such as:

- How is the platform performing?
- Is revenue increasing over time?
- How many transactions are being processed?
- Is fraud increasing?
- Which states contribute the highest business volume?

---

## KPIs

The dashboard highlights the primary business metrics:

- Total Revenue
- Total Transactions
- Average Transaction Value
- Fraud Rate
- Fraud Transactions
- Average Fraud Transactions

These KPIs provide an instant snapshot of overall platform health.

---

## Monthly Revenue Trend

**Business Question**

> Is revenue growing consistently over time?

**Purpose**

Monitor revenue performance and identify seasonal trends.

**Business Value**

Helps leadership evaluate business growth and identify periods requiring further investigation.

---

## Monthly Transaction Volume Trend

**Business Question**

> Are transaction volumes increasing?

**Purpose**

Shows customer activity throughout the reporting period.

**Business Value**

Supports demand forecasting and infrastructure planning.

---

## Monthly Fraud Trend

**Business Question**

> Is fraud activity increasing?

**Purpose**

Tracks fraudulent transactions over time.

**Business Value**

Allows fraud teams to quickly identify abnormal spikes requiring investigation.

---

## Revenue by State

**Business Question**

> Which geographic regions generate the highest revenue?

**Purpose**

Visualizes revenue contribution across states.

**Business Value**

Supports regional performance analysis and market expansion decisions.

---

## Transaction Volume by State

**Business Question**

> Which states process the highest transaction volume?

**Purpose**

Identifies regions with the greatest customer activity.

**Business Value**

Helps operations allocate resources based on transaction demand.

---

## Fraud Rate by State

**Business Question**

> Which states experience higher fraud rates?

**Purpose**

Highlights geographic fraud concentration.

**Business Value**

Allows risk teams to prioritize fraud monitoring in high-risk regions.

---

![alt text](<Merchant Analyics.png>)

# Merchant Analytics

## Objective

Evaluate merchant performance while balancing revenue generation against fraud exposure.

This report helps answer:

- Which merchant categories generate the most revenue?
- Which categories process the highest transaction volume?
- Which merchant categories contribute most to fraud?
- Which merchants require additional fraud monitoring?

---

## Top Merchant Categories Contributing to Revenue

**Business Question**

> Which merchant categories drive platform revenue?

**Purpose**

Ranks merchant categories by revenue contribution.

**Business Value**

Identifies strategic business segments that generate the largest share of revenue.

---

## Top Merchant Categories Contributing to Fraud

**Business Question**

> Which merchant categories contribute most to fraudulent transactions?

**Purpose**

Displays fraud distribution across merchant categories.

**Business Value**

Supports targeted fraud prevention strategies.

---

## Transaction Volume vs Revenue

**Business Question**

> Do merchant categories with higher transaction volume also generate higher revenue?

**Purpose**

Compares transaction count with revenue contribution.

**Business Value**

Distinguishes between high-volume and high-value merchant categories, enabling more informed commercial decisions.

---

## Top Merchants by Revenue & Fraud Rate

**Business Question**

> Which merchants generate high revenue while maintaining acceptable fraud levels?

**Purpose**

Compares merchant revenue alongside fraud rate.

**Business Value**

Helps identify merchants requiring enhanced fraud monitoring without negatively impacting valuable business relationships.

---

## Merchant Performance Table

The detailed table provides merchant-level metrics including:

- Revenue
- Transactions
- Fraud Transactions
- Fraud Rate

This enables users to drill into individual merchant performance beyond the summary visuals.

---

![alt text](<Customer Analytics.png>)

# Customer Analytics

## Objective

Understand customer spending behaviour, transaction patterns, and fraud activity throughout the day.

This report answers questions such as:

- When are customers most active?
- Which hours generate the highest revenue?
- When does fraud occur most frequently?
- Which occupations contribute the most spending?
- Which occupations experience higher fraud activity?

---

## Transaction Volume by Hour

**Business Question**

> During which hours are customers most active?

**Purpose**

Displays transaction volume across the day.

**Business Value**

Supports operational planning, infrastructure scaling, and customer support staffing.

---

## Revenue by Hour

**Business Question**

> During which hours is the highest revenue generated?

**Purpose**

Shows hourly revenue distribution.

**Business Value**

Helps understand customer purchasing behaviour and peak business periods.

---

## Fraud Transactions by Hour

**Business Question**

> When does fraud activity occur most frequently?

**Purpose**

Visualizes hourly fraud patterns.

**Business Value**

Allows fraud operations teams to focus monitoring efforts during higher-risk periods.

---

## Top Occupations Contributing to Fraud

**Business Question**

> Which customer occupations contribute the highest number of fraudulent transactions?

**Purpose**

Ranks occupations based on fraud activity.

**Business Value**

Supports behavioural analysis and can guide future customer segmentation studies.

---

## Spending by Occupation and Gender

**Business Question**

> How does spending vary across occupations and gender?

**Purpose**

Compares customer spending across demographic segments.

**Business Value**

Helps identify valuable customer segments that may benefit from targeted marketing or premium financial products.

---

# Key Business Outcomes

The dashboard enables stakeholders to:

- Monitor overall payment platform performance.
- Track revenue and transaction growth trends.
- Identify geographic regions driving business performance.
- Detect fraud concentration across states and merchant categories.
- Evaluate merchant performance using both commercial and risk metrics.
- Understand customer transaction behaviour throughout the day.
- Identify customer segments with higher spending or fraud activity.
- Support data-driven operational and strategic decision making through interactive Power BI reporting.