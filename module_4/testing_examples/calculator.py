"""A simple calculator module to demonstrate various testing approaches."""

import asyncio
from typing import Union

CalculatorDigitT = Union[int, float]


class Calculator:
    """Calculator class with basic arithmetic operations and some async capabilities."""

    def __init__(self):
        self.history = []

    def add(self, a: CalculatorDigitT, b: CalculatorDigitT) -> CalculatorDigitT:
        """Add two numbers and store the operation in history."""
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result

    def divide(self, a: CalculatorDigitT, b: CalculatorDigitT) -> CalculatorDigitT:
        """Divide a by b, raising ValueError for division by zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self.history.append(f"Divided {a} / {b} = {result}")
        return result

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history = []

    async def delayed_add(
        self, a: CalculatorDigitT, b: CalculatorDigitT, delay: float = 0.1
    ) -> CalculatorDigitT:
        """Asynchronously add two numbers after a delay."""
        await asyncio.sleep(delay)
        return self.add(a, b)


class CalculatorAPI:
    """Mock API client for demonstrating dependency injection and mocking."""

    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def perform_calculation(
        self, operation: str, a: CalculatorDigitT, b: CalculatorDigitT
    ) -> CalculatorDigitT:
        """Perform a calculation based on the operation type."""
        if operation == "add":
            return self.calculator.add(a, b)
        elif operation == "divide":
            return self.calculator.divide(a, b)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
