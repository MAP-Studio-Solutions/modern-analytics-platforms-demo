# Workforce Analytics — Domain Overview

The Workforce Analytics domain models the core entities, events, and historical changes that describe an organization’s employees over time.  
It provides a governed, point‑in‑time view of the workforce suitable for reporting, BI consumption, and downstream analytics.

This README describes the **business domain**, **data model**, and **analytical outputs**.  
Execution details are defined separately in each method folder.

---

## Domain Purpose

The Workforce domain answers foundational questions about an organization’s people:

- How many employees do we have today?
- How has headcount changed over time?
- Which departments are growing or shrinking?
- What events (hire, termination, transfer, promotion) drive those changes?
- What is the historical composition of the workforce at any point in time?

The domain is intentionally small but representative of real enterprise workforce systems.

---

## Domain Entities

### **Employee**
The central entity representing a worker in the organization.  
Attributes include:

- employee_id  
- name  
- department  
- job role  
- manager  
- employment status  
- effective dates (for SCD2 history)

### **Department**
Organizational structure used for grouping and reporting.  
Attributes include:

- department_id  
- department_name  
- parent_department (optional)

### **Job**
Represents the employee’s role or position.  
Attributes include:

- job_id  
- job_title  
- job_family  
- job_level

---

## Domain Events

The domain models key workforce events that change the composition of the organization:

- **Hire**  
- **Termination**  
- **Transfer**  
- **Promotion**  
- **Compensation change**  

These events feed both SCD2 history and point‑in‑time headcount reconstruction.

---

## Gold‑Layer Data Model

The Workforce domain produces a small but durable dimensional model.

### **Dimensions**

#### `dim_employee` (SCD Type 2)
Tracks employee attributes over time using effective‑date logic.  
Supports point‑in‑time reporting and historical reconstruction.

#### `dim_date`
Standard calendar dimension used for time‑series alignment.

### **Facts**

#### `fact_employee_events`
A conformed event table representing hires, terminations, transfers, promotions, and compensation changes.

#### `fact_headcount_snapshot`
A point‑in‑time table that reconstructs workforce composition for any historical date.

---

## Modeling Patterns

The Workforce domain uses:

- **SCD Type 2** for employee history  
- **Point‑in‑time reconstruction** for headcount  
- **Surrogate keys** for dimensional stability  
- **Effective‑date logic** for historical accuracy  
- **Event‑driven modeling** for workforce changes  

These patterns mirror real enterprise workforce analytics systems.

---

## How This Domain Relates to Methods

This domain can be implemented using multiple execution methods:

- **Databricks‑Native** (SQL‑first ELT)
- **dbt‑Databricks** (model‑first DAG)
- **Genie** (semantic‑layer‑first AI querying)

Each method produces or consumes the **same gold‑layer model**, but uses a different execution approach.

See the method folders for implementation details.

