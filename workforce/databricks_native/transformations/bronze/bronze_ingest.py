from __future__ import annotations
from pyspark.sql import SparkSession, functions as F


def ingest_to_bronze(
    spark: SparkSession,
    landing_path: str,
    bronze_path: str,
    spec
) -> None:
    """
    Generic bronze ingestion:
    - Reads raw landing files
    - Applies minimal normalization
    - Adds ingestion metadata
    - Writes append-only Delta to bronze
    """

    # Construct full paths
    full_landing = f"{landing_path}/{spec.landing_relpath}"
    full_bronze  = f"{bronze_path}/{spec.bronze_table}"

    print(f"Reading landing data: {full_landing}")

    # Read raw landing data
    df = (
        spark.read.format(spec.format)
            .option("header", "true")
            .load(full_landing)
            .withColumn("_ingest_ts", F.current_timestamp())
            .withColumn("_file_path", F.input_file_name())
            .withColumn("_load_id", F.expr("uuid()"))
    )

    print(f"Writing bronze table: {full_bronze}")

    (
        df.write
          .format("delta")
          .mode("append")
          .save(full_bronze)
    )

    print(f"Bronze load complete: {spec.name} → {full_bronze}")
