{%- macro current_timestamp() -%}
    {{ adapter.dispatch('current_timestamp', 'dbt')() }}
{%- endmacro -%}

{% macro default__current_timestamp() %}
    current_timestamp
{% endmacro %}

{%- macro current_timestamp_in_utc() -%}
    {{ adapter.dispatch('current_timestamp_in_utc', 'dbt')() }}
{%- endmacro -%}

{% macro default__current_timestamp_in_utc() %}
    {{ default__current_timestamp() }} at time zone 'utc'
{% endmacro %}

{%- macro snapshot_get_time() -%}
    {{ adapter.dispatch('snapshot_get_time', 'dbt')() }}
{%- endmacro -%}

{% macro default__snapshot_get_time() %}
    {{ current_timestamp() }}
{% endmacro %}

{%- macro convert_timezone(timestamp,  target_tz, source_tz) -%}
    {%- if not target_tz is string -%}
        {{ exceptions.raise_compiler_error("'target_tz' must be a string") }}
    {%- else -%}
        {{ adapter.dispatch('convert_timezone', 'dbt') (column, target_tz, source_tz) }}
    {%- endif -%}

{%- endmacro -%}

{%- macro default__convert_timezone(column, target_tz, source_tz) -%}
    {%- if not source_tz -%}
        {{ column }} at time zone '{{ target_tz }}'
    {%- else -%}
        {{ column }} at time zone '{{ source_tz }}' at time zone '{{ target_tz }}'
    {%- endif -%}
{%- endmacro -%}

{%- macro now(tz=None) -%}
{{ convert_timezone(current_timestamp_in_utc(), tz) }}
{%- endmacro -%}

