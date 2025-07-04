from sqlalchemy import Table, Column, Integer, String, Float, Text, Boolean
from app.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("telegram_id", Integer, unique=True, nullable=False),
    Column("username", String, nullable=True),
)

listings = Table(
    "listings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("district", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("description", Text, nullable=True),
    Column("photo_file_id", String, nullable=True),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
    Column("is_paid", Boolean, default=False),
)