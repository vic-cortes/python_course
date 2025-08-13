# Curso Python

Un curso completo de Python para desarrolladores experimentados, enfocado en buenas prácticas y desarrollo profesional.

# Python Course - Professional Development

A comprehensive Python course for experienced developers, focusing on best practices and professional development.

## Project Description

This repository contains a comprehensive Python course covering fundamental concepts through advanced development practices. The course includes practical examples, exercises, and a real-world web scraping project for price monitoring.

## Project Structure

```
.
├── module_1/          # Python fundamentals and basic syntax
├── module_2/          # Functions, modules and data handling
├── module_4/          # Virtual environments, testing and code quality
├── project/          # Web scraping practical project
└── slidev/           # Presentations and learning materials
```

## Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (for web scraping project)
- Visual Studio Code (recommended)
- Recommended extensions:
  - [DrawIO](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) - For diagram visualization

## Core Dependencies

### Development Tools
- uv (package and virtual environment manager)
- ruff (linter and formatter)
- pytest (testing)
- ipython/jupyter (interactive environment)

### Web Scraping Project
- FastAPI
- SQLAlchemy
- Alembic
- BeautifulSoup4
- Selenium
- Pandas

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository_URL]
cd python_course
```

2. Create and activate virtual environment with uv:
```bash
uv venv
source .venv/bin/activate  # On Unix/MacOS
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
cd project
uv pip install -e .
```

## Module Structure

### Module 1: Python Fundamentals
- Basic syntax
- Data types and structures
- PEP 8 and code style
- Practical exercises

### Module 2: Functions and Modules
- Functions and decorators
- Module management
- Examples with Flask and Pydantic

### Module 4: Professional Tools
- Virtual environments (venv, poetry, uv)
- Testing (unittest, pytest)
- Code quality and linting

## Practical Project: Web Scraping

The project includes a real-world web scraping application for price monitoring, demonstrating:
- Modular architecture
- FastAPI and SQLAlchemy
- Alembic migrations
- Docker and Docker Compose
- Testing and best practices

### Project Commands

```bash
# Start the database
make db_up

# Verify database connection
make test_db_connection

# Create new migrations
make db-create-migrations message="your message here"

# Start API server
make run_api

# Check code quality
make ruff_check
```

## Usage Examples

### Testing with pytest
```python
# test_calculator_pytest.py
def test_addition():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5
```

### API Endpoints
```python
# Check service health
GET /health

# Get data from specific scraper
GET /data/{scraper_name}
```

## Additional Documentation

- [Testing Module](module_4/testing_examples/README.md)
- [Dependency Management with UV](module_4/virtual_environments/uv_example/README.md)
- [Web Scraping Project Documentation](project/README.md)

## Legal Considerations

The code in this repository is available for educational and reference purposes. The web scraping project includes considerations for responsible and ethical scraping practices.

## License

This project is distributed under the MIT License. See the LICENSE file for more details.