"""Integration tests demonstrating testing of multiple components together."""

import asyncio

import pytest
from calculator import Calculator, CalculatorAPI


class TestCalculatorIntegration:
    """Integration tests for Calculator and CalculatorAPI."""

    @pytest.fixture
    def calculator(self):
        """Provide a Calculator instance."""
        return Calculator()

    @pytest.fixture
    def api(self, calculator):
        """Provide a CalculatorAPI instance with real Calculator."""
        return CalculatorAPI(calculator)

    def test_multiple_operations(self, api, calculator):
        """Test multiple operations and verify history."""
        # Perform calculations via API
        api.perform_calculation("add", 5, 3)
        api.perform_calculation("divide", 16, 4)

        # Verify history in underlying calculator
        assert len(calculator.history) == 2
        assert "Added 5 + 3 = 8" in calculator.history
        assert "Divided 16 / 4 = 4.0" in calculator.history

    def test_error_propagation(self, api):
        """Test that errors properly propagate through the API."""
        with pytest.raises(ValueError) as exc_info:
            api.perform_calculation("divide", 10, 0)
        assert "Division by zero" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_async_operations(self, calculator):
        """Test multiple async operations."""
        # Perform multiple async operations concurrently
        tasks = [calculator.delayed_add(i, i, delay=0.01) for i in range(5)]
        results = await asyncio.gather(*tasks)

        # Verify results
        assert results == [0, 2, 4, 6, 8]
        assert len(calculator.history) == 5
