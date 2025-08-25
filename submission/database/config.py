from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Baca DATABASE_URL dari .env atau default ke SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./employees.db")

# SQLite perlukan special connect_args
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Engine
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk models
Base = declarative_base()
