{% macro cast_array_to_string(array) %}
  {{ adapter.dispatch('cast_array_to_string', 'dbt') (array) }}
{% endmacro %}

{% macro default__cast_array_to_string(array) %}
    cast({{ array }} as {{ type_string() }})
{% endmacro %}
