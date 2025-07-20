"""Test cases for calculator module using pytest framework."""

import pytest
from calculator import Calculator, CalculatorAPI


# Fixtures
@pytest.fixture
def calculator():
    """Provide a Calculator instance."""
    return Calculator()


@pytest.fixture
def calculator_api(calculator):
    """Provide a CalculatorAPI instance with a Calculator dependency."""
    return CalculatorAPI(calculator)


@pytest.fixture
def populated_calculator():
    """Provide a Calculator instance with some history."""
    calc = Calculator()
    calc.add(2, 2)
    calc.add(3, 3)
    return calc


# Basic test cases with fixtures
def test_calculator_initial_state(calculator):
    """Test the initial state of Calculator instance."""
    assert len(calculator.history) == 0


def test_calculator_add(calculator: Calculator):
    """Test the add method."""
    result = calculator.add(1, 1)
    assert result == 2
    assert len(calculator.history) == 1


# Parameterized tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add_parameterized(calculator: Calculator, a, b, expected):
    """Test add method with various inputs."""
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (15, 3, 5),
        (1, 4, 0.25),
    ],
)
def test_divide_parameterized(calculator, a, b, expected):
    """Test divide method with various inputs."""
    assert calculator.divide(a, b) == expected


# Testing exceptions
def test_divide_by_zero(calculator):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


# Mocking examples
def test_api_with_mock_calculator(mocker):
    """Test CalculatorAPI with a mocked Calculator."""
    # Create mock calculator with configured methods
    mock_calc = mocker.Mock(spec=Calculator)
    mock_calc.add.return_value = 42
    mock_calc.divide.return_value = 5

    api = CalculatorAPI(mock_calc)

    # Test add operation
    result = api.perform_calculation("add", 5, 5)
    assert result == 42
    mock_calc.add.assert_called_once_with(5, 5)

    # Test divide operation
    result = api.perform_calculation("divide", 10, 2)
    assert result == 5
    mock_calc.divide.assert_called_once_with(10, 2)

    # Test invalid operation
    with pytest.raises(ValueError):
        api.perform_calculation("multiply", 5, 5)


# Async test example
@pytest.mark.asyncio
async def test_delayed_add(calculator):
    """Test the async delayed_add method."""
    result = await calculator.delayed_add(2, 3, delay=0.01)
    assert result == 5
    assert len(calculator.history) == 1


# Test class demonstrating shared fixtures
class TestCalculatorHistory:
    """Test cases focused on calculator history functionality."""

    def test_history_length(self, populated_calculator):
        """Test the number of history entries."""
        assert len(populated_calculator.history) == 2

    def test_clear_history(self, populated_calculator):
        """Test clearing the history."""
        populated_calculator.clear_history()
        assert len(populated_calculator.history) == 0


# Edge cases and boundary testing
@pytest.mark.parametrize(
    "a, b",
    [
        (float("inf"), 1),
        (1, float("inf")),
        (float("-inf"), 1),
        (1e308, 1e308),  # Very large numbers
    ],
)
def test_add_edge_cases(calculator, a, b):
    """Test add method with edge cases."""
    calculator.add(a, b)  # Just verify no exceptions are raised
