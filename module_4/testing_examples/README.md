# Python Testing Examples

This directory contains comprehensive examples of testing in Python using both `unittest` and `pytest` frameworks. The examples demonstrate various testing patterns, techniques, and best practices.

## Project Structure

- `calculator.py` - Main module containing the code under test
- `test_calculator_unittest.py` - Examples using Python's built-in unittest framework
- `test_calculator_pytest.py` - Examples using pytest with advanced features
- `test_integration.py` - Integration test examples
- `pytest.ini` - Pytest configuration including coverage settings
- `requirements.txt` - Project dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests with coverage:
```bash
pytest
```

Run specific test file:
```bash
pytest test_calculator_pytest.py
```

## Testing Examples Demonstrated

### Basic Assertions and Test Methods
- Basic assertions using both unittest and pytest styles
- Test method organization and naming conventions
- Test class structure and inheritance

### Test Fixtures and Setup/Teardown
- unittest setUp and tearDown methods
- pytest fixtures with different scopes
- Fixture composition and dependency injection

### Parameterized Testing
- pytest.mark.parametrize for data-driven testing
- Testing with multiple inputs and edge cases
- Boundary testing examples

### Mocking and Patching
- Using unittest.mock and pytest-mock
- Mocking dependencies and external services
- Dependency injection patterns

### Exception Testing
- Testing error conditions
- Exception message validation
- Context manager-based tests

### Async Testing
- Testing coroutines and async functions
- pytest.mark.asyncio usage
- Concurrent operation testing

### Test Organization
- Test discovery and collection
- Test categorization with markers
- Integration vs unit test separation

### Coverage Reporting
- Coverage configuration in pytest.ini
- HTML and terminal coverage reports
- Missing coverage identification

## Best Practices Demonstrated

1. Test Isolation
   - Each test is independent
   - Clean setup and teardown
   - No test interdependencies

2. Clear Test Names
   - Descriptive test method names
   - Clear test purpose documentation
   - Well-structured test organization

3. Comprehensive Testing
   - Edge cases covered
   - Error conditions tested
   - Boundary values considered

4. DRY Principles
   - Fixture reuse
   - Parameterized testing
   - Shared setup when appropriate

5. Integration Testing
   - Component interaction testing
   - System behavior verification
   - Error propagation testing

## Key Features

### Calculator Module
- Basic arithmetic operations
- Operation history tracking
- Async calculation support
- Error handling
- API wrapper demonstration

### Testing Approaches
1. **Unit Testing**
   - Individual component testing
   - Function-level validation
   - Isolated dependency testing

2. **Integration Testing**
   - Component interaction testing
   - End-to-end scenarios
   - Real dependency usage

3. **Async Testing**
   - Coroutine testing
   - Concurrent operation validation
   - Async fixture usage

4. **Edge Case Testing**
   - Boundary conditions
   - Error scenarios
   - Special value handling

## Code Coverage

The project is configured with pytest-cov to generate coverage reports. Run tests to see:
- Line-by-line coverage in terminal
- HTML coverage report
- Missing coverage identification

## Future Enhancements

Potential areas for expanding the examples:
1. Property-based testing with hypothesis
2. Performance testing examples
3. Behavior-driven development (BDD) style tests
4. Database integration testing
5. Web API testing examples