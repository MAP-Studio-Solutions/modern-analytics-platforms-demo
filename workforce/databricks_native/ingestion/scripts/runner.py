from __future__ import annotations
from pyspark.sql import SparkSession

from .config import load_sources_yaml
from workforce.databricks_native.transformations.bronze.bronze_ingest import ingest_to_bronze


def run_ingestion(
    sources_yaml: str,
    landing_path: str,
    bronze_path: str
) -> None:
    """
    Databricks-side ingestion runner.
    Loads source specs from YAML and ingests each source into bronze.
    """

    spark = SparkSession.builder.getOrCreate()

    sources = load_sources_yaml(sources_yaml)
    print(f"Loaded {len(sources)} sources from {sources_yaml}")

    for spec in sources.values():
        print(f"Ingesting {spec.name}...")
        ingest_to_bronze(
            spark=spark,
            landing_path=landing_path,
            bronze_path=bronze_path,
            spec=spec
        )
