from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


database_url = "postgresql://postgres:postgres@localhost/rental_db"

engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()