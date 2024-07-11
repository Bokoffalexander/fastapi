from fastapi import FastAPI
from fastapi import Depends
from schemas import STaskAdd
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")


from router import router as tasks_router

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
   return {"go": "tasks"}

app.include_router(tasks_router)
