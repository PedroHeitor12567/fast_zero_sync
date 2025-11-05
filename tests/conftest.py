import pytest
from fastapi.testclient import TestClient

from projeto_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
