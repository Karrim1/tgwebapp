import asyncio
from fastapi import FastAPI
from app.database import database, metadata, engine
from app.bot import main as bot_main
from sqlalchemy import create_engine

app = FastAPI()

# Создаем таблицы при старте (опционально)
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()
    asyncio.create_task(bot_main())

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()