from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

synonyms = Table(
    "synonyms",
    metadata,
    Column("first_string", String, nullable=False),
    Column("second_string", String, nullable=True)

)

