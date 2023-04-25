SELECT id
FROM {{ ref('my_second_dbt_model') }}
GROUP BY id
HAVING (id = 0)