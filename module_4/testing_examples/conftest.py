"""Configuration file for pytest with async support."""

import pytest

# Configure pytest-asyncio to use strict mode and auto-use fixtures
pytest_plugins = ["pytest_asyncio"]


@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for each test case."""
    import asyncio

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
