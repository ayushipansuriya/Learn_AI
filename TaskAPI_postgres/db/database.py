from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL DB
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)





SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()