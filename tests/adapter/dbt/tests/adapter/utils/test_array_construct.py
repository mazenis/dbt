import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_array_construct import (
    seeds__data_array_construct_csv,
    models__test_array_construct_sql,
    models__test_array_construct_yml,
)


class BaseArrayConstruct(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "data_array_construct.csv": seeds__data_array_construct_csv,
        }

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_array_construct.yml": models__test_array_construct_yml,
            "test_array_construct.sql": self.interpolate_macro_namespace(
                models__test_array_construct_sql, "array_construct"
            ),
        }


class TestArrayConstruct(BaseArrayConstruct):
    pass
