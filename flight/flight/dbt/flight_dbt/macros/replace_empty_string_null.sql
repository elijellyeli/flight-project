{#
    This macro replaces the empty string with null
#}

{% macro replace_empty_string_null(col_name) -%}
    case 
        when {{ col_name }} = '' then null
        else {{ col_name }}
    end as {{ col_name }}
{%- endmacro %}