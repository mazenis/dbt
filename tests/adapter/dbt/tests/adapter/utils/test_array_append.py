import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_array_append import (
    seeds__data_array_append_csv,
    models__test_array_append_sql,
    models__test_array_append_yml,
)
from dbt.tests.adapter.utils.fixture_array_construct import (
    seeds__data_array_construct_csv,
)


class BaseArrayAppend(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "data_array_append.csv": seeds__data_array_append_csv,
            "data_array_construct.csv": seeds__data_array_construct_csv,
        }

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_array_append.yml": models__test_array_append_yml,
            "test_array_append.sql": self.interpolate_macro_namespace(
                models__test_array_append_sql, "array_append"
            ),
        }


class TestArrayAppend(BaseArrayAppend):
    pass
