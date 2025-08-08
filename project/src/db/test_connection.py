from session import engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

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
