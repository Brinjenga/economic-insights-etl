import great_expectations as ge
from pyspark.sql import DataFrame

def validate_with_great_expectations(df: DataFrame, expected_schema: dict, unique_cols=None):
    """
    Validate a Spark DataFrame using Great Expectations: nulls, uniqueness, schema.
    Args:
        df: PySpark DataFrame
        expected_schema: dict of {col: type}
        unique_cols: list of columns to check uniqueness
    Returns:
        None. Raises AssertionError if validation fails.
    """
    pdf = df.toPandas()
    ge_df = ge.from_pandas(pdf)
    for col in expected_schema:
        ge_df.expect_column_values_to_not_be_null(col)
    if unique_cols:
        for col in unique_cols:
            ge_df.expect_column_values_to_be_unique(col)
    for col, dtype in expected_schema.items():
        ge_df.expect_column_values_to_be_of_type(col, dtype)
    results = ge_df.validate()
    if not results['success']:
        raise ValueError(f"Great Expectations validation failed: {results}")
