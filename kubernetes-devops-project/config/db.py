from sqlalchemy import create_engine, MetaData
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:password@db:5432/storedb")
engine = create_engine(DATABASE_URL)

meta = MetaData()

conn = engine.connect()
