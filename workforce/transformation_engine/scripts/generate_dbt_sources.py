import yaml
from pathlib import Path

# Paths relative to this script
INGESTION_YAML = Path("../../ingestion_engine/sources.yaml")
OUTPUT_YAML = Path("../models/sources/workforce_landing.yml")

LANDING_ROOT = "abfss://analytics@stanalyticsdl001.dfs.core.windows.net/workforce/landing"


def load_ingestion_sources(path: Path) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)["sources"]


def build_dbt_sources_yaml(sources: dict) -> dict:
    tables = []

    for name, spec in sources.items():
        # Strip filename from landing_relpath
        folder = "/".join(spec["landing_relpath"].split("/")[:-1])

        tables.append({
            "name": name,
            "external": {
                "location": f"{LANDING_ROOT}/{folder}",
                "file_format": spec["format"]
            }
        })

    return {
        "version": 2,
        "sources": [
            {
                "name": "workforce_landing",
                "tables": tables
            }
        ]
    }


def write_yaml(path: Path, content: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(content, f, sort_keys=False)


def main():
    sources = load_ingestion_sources(INGESTION_YAML)
    dbt_yaml = build_dbt_sources_yaml(sources)
    write_yaml(OUTPUT_YAML, dbt_yaml)
    print(f"Generated dbt source YAML at: {OUTPUT_YAML}")


if __name__ == "__main__":
    main()
