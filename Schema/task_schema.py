from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    id: Optional[int]
    tittle: str
    description: str
    state: str
    