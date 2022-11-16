from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import DB_NAME, DB_PASSWORD, DB_HOST, DB_USER

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:3214@localhost:5432/test_db" 
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocsommit=False, autoflush=False, bind=engine)

Base = declarative_base()
