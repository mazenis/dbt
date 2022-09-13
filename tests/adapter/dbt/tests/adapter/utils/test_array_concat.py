import pytest
from dbt.tests.adapter.utils.base_utils import BaseUtils
from dbt.tests.adapter.utils.fixture_array_concat import (
    seeds__data_array_concat_csv,
    models__test_array_concat_sql,
    models__test_array_concat_yml,
)
from dbt.tests.adapter.utils.fixture_array_construct import (
    seeds__data_array_construct_csv,
)


class BaseArrayConcat(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "data_array_concat.csv": seeds__data_array_concat_csv,
            "data_array_construct.csv": seeds__data_array_construct_csv,
        }

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_array_concat.yml": models__test_array_concat_yml,
            "test_array_concat.sql": self.interpolate_macro_namespace(
                models__test_array_concat_sql, "array_concat"
            ),
        }


class TestArrayConcat(BaseArrayConcat):
    pass
