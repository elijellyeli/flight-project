
/*
    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

WITH source_data AS (
    SELECT 1 AS id
    UNION ALL
    SELECT 2 AS id
)

SELECT *
FROM source_data