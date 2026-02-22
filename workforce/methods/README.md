# Workforce Analytics — Method Index

This project demonstrates the Workforce Analytics domain implemented through **multiple execution methods**, each reflecting a different way organizations build and operate data pipelines.  
A *method* is not a domain or a dataset — it is an **execution approach** for producing the same gold‑layer analytical outputs.

Each method folder contains its own README with full execution details.  
This index provides a simple, high‑level description of each method.

---

## Databricks‑Native Method
A SQL‑first ELT approach built directly on Databricks using Workflows, Delta Lake, and medallion‑layer SQL.  
It emphasizes transparency, deterministic transformations, and direct control over ingestion, SCD2 logic, and PIT reconstruction.  
This method is closest to how many teams modernize legacy SQL pipelines into governed lakehouse patterns.

**See:** `workforce/databricks-native/README.md`

---

## dbt‑Databricks Method
A model‑driven approach using dbt to define sources, staging models, intermediate logic, snapshots, and marts.  
dbt handles dependency management, testing, documentation, and SCD2 via snapshots, while Databricks provides the execution engine.  
This method reflects how modern analytics teams standardize transformations using dbt’s DAG and testing framework.

**See:** `workforce/databricks-dbt/README.md`

---

## Genie (Semantic Layer) Method
An AI‑assisted analytics method that uses Unity Catalog semantic models to translate natural language into SQL.  
Genie does not ingest or transform data — it sits on top of the gold layer and provides conversational analytics powered by governed metadata.  
This method demonstrates how semantic modeling enables AI‑driven querying and exploration.

**See:** `workforce/databricks-genie/README.md`

---

## How These Methods Relate
All methods produce or consume the **same gold‑layer analytical model**, but each demonstrates a different execution philosophy:

- **Databricks‑Native:** SQL‑first, workflow‑orchestrated pipelines  
- **dbt‑Databricks:** model‑first, DAG‑driven transformations  
- **Genie:** semantic‑layer‑first, AI‑assisted querying  

This structure allows the project to show multiple valid approaches to implementing the same domain.

