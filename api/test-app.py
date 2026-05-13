import pytest
from app import app

@pytest.fixture
yield app


