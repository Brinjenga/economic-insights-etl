from pyspark.sql import SparkSession
from .validation import validate_with_great_expectations

def transform_and_validate_bronze_to_silver(input_path, output_path, expected_schema, unique_cols=None):
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.parquet(input_path)
    validate_with_great_expectations(df, expected_schema, unique_cols)
    # ...additional transformation logic...
    df.write.mode("overwrite").parquet(output_path)