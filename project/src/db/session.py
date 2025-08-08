import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(override=True)


class DbConfig:
    DATABASE_USERNAME = os.getenv("POSTGRES_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    DATABASE_NAME = os.getenv("POSTGRES_DB", "scraper")
    DATABASE_HOST = os.getenv("POSTGRES_HOST", "localhost")
    DATABASE_PORT = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )


# Create an SQLAlchemy engine
engine = create_engine(DbConfig.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
