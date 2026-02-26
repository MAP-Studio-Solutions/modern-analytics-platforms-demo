{{ config(
    materialized = 'table',
    schema = 'workforce',
    alias = 'bronze_placeholder'
) }}

-- Bronze Placeholder Model
-- -------------------------
-- This model exists only to validate that the dbt project compiles
-- and that the Bronze layer is wired correctly.
--
-- Replace this with real Bronze ingestion logic once landing files
-- and source definitions are finalized.

select
    current_timestamp() as loaded_at,
    'bronze_placeholder' as model_name,
    'replace this with real bronze logic' as note
