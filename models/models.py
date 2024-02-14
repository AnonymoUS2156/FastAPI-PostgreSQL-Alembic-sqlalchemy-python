from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

synonyms = Table(
    "synonym",
    metadata,
    Column("first_synonym", String, nullable=False),
    Column("second_synonym", String, nullable=True)
)
