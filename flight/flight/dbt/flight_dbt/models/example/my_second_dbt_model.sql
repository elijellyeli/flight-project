
-- Use the `ref` function to select from other models
SELECT
    a.*
    , b.*
FROM {{ ref('my_first_dbt_model') }} AS a

LEFT JOIN {{ source('mage_demo', 'dbt_demo_pipeline_load_data') }} AS b
ON 1 = 1

WHERE a.id = 1