import os

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

from .session import engine

# TODO - move this into postgres_utils.py


# Retrieve the connection string from environment variables
connection_string = os.getenv("POSTGRES_CONNECTION_STRING")

# Create an SQLAlchemy engine
try:

    # Connect to the database
    with engine.connect() as connection:
        # Prepare a SQL statement for execution
        stmt = text("SELECT 1")

        # Execute the SQL statement
        result = connection.execute(stmt)
        output = result.scalar()

        # Check if the result of the query is as expected
        if output == 1:
            print("Database connection established successfully.")

except SQLAlchemyError as e:
    print(f"An error occurred: {e}")
