{# when casting as array to string, postgres uses {} (ex: {1,2,3}) while other dbs use [] (ex: [1,2,3]) #}
{% macro postgres__cast_array_to_string(array) %}
    {%- set array_as_string -%}cast({{ array }} as {{ type_string() }}){%- endset -%}
    {{ replace(replace(array_as_string,"'}'","']'"),"'{'","'['") }}
{% endmacro %}
