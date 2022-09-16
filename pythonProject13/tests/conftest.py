import pytest

from pythonProject13.run import app


@pytest.fixture()
def test_client():
    return app.test_client()
