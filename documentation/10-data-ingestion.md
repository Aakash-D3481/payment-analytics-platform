## Implementation Summary

The ingestion layer was implemented using an event-driven AWS Lambda function triggered whenever a CSV file is uploaded to the Raw zone of the S3 data lake.

The Lambda function performs lightweight validation before ETL processing begins.

Validation checks include:

- File extension validation
- Required column validation using an external schema configuration
- Duplicate header detection
- File metadata retrieval (size and last modified timestamp)

To improve scalability, the Lambda function reads only the CSV header instead of loading the entire dataset into memory. Heavy processing is intentionally delegated to AWS Glue.

This design minimizes memory usage, reduces execution time, and aligns with serverless best practices for large datasets.