import boto3
import csv
import json
import logging
from io import StringIO

# AWS Clients
s3 = boto3.client("s3")

# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def load_schema_config(bucket_name):
    """
    Reads schema.json from the config folder in S3.
    Returns the required column list.
    """

    response = s3.get_object(
        Bucket=bucket_name,
        Key="config/schema.json"
    )

    schema = json.loads(
        response["Body"].read().decode("utf-8")
    )

    return schema

def load_pipeline_config(bucket_name):

    response = s3.get_object(
        Bucket=bucket_name,
        Key="config/pipeline_config.json"
    )

    config = json.loads(
        response["Body"].read().decode("utf-8")
    )

    return config

def read_csv_from_s3(bucket_name, object_key):

    response = s3.get_object(
        Bucket=bucket_name,
        Key=object_key
    )

    csv_content = response["Body"].read().decode("utf-8")

    return csv_content

def validate_file_type(object_key):

    if not object_key.endswith(".csv"):
        raise ValueError("Only CSV files are allowed.")

def validate_required_columns(csv_content, required_columns):

    reader = csv.reader(StringIO(csv_content))

    headers = next(reader)

    missing_columns = [
        column
        for column in required_columns
        if column not in headers
    ]

    if missing_columns:

        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return headers

def validate_duplicate_headers(headers):

    if len(headers) != len(set(headers)):
        raise ValueError(
            "Duplicate column names found."
        )

def count_records(csv_content):

    reader = csv.reader(StringIO(csv_content))

    next(reader)

    row_count = sum(1 for _ in reader)

    return row_count