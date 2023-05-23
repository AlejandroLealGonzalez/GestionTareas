from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from Config.db import engine, meta_data

tasks = Table(
    "tasks",meta_data,
    Column("id", Integer, primary_key=True),
    Column("tittle",String(255),nullable=False),
    Column("description",String(255),nullable=False),
    Column("state",String(255),nullable=False),
)

meta_data.create_all(engine)