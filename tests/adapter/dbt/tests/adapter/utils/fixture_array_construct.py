# array_construct

seeds__data_array_construct_csv = """num_input_1,num_input_2,num_input_3,result_as_string
1,2,3,"[1,2,3]"
4,5,6,"[4,5,6]"
"""


models__test_array_construct_sql = """
with data as (

    select * from {{ ref('data_array_construct') }}

),

array_construct as (
    select
        {{ array_construct(['num_input_1', 'num_input_2', 'num_input_3']) }} as array_actual,
        result_as_string as expected

    from data

    union all

    select
        {{ array_construct() }} as array_actual,
        '[]' as expected

)

-- we need to cast the arrays to strings in order to compare them to the output in our seed file
select
    array_actual,
    {{ cast_array_to_string('array_actual') }} as actual,
    expected
from array_construct
"""


models__test_array_construct_yml = """
version: 2
models:
  - name: test_array_construct
    tests:
      - assert_equal:
          actual: actual
          expected: expected
"""
