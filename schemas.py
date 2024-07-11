from pydantic import BaseModel, ConfigDict
from fastapi import Depends

class STaskAdd(BaseModel):

   name: str
   description: str | None = None

class STask(STaskAdd):
   id: int
   model_config = ConfigDict(from_attributes=True)

#@app.post("/")
#async def add_task(task: STaskAdd = Depends()):
#   return {"data": task}

class STaskId(BaseModel):
   id: int
