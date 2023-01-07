from itertools import count
from typing import Optional
from pydantic import BaseModel, Field


c = count()

class PessoaModelo(BaseModel):
    id: Optional[int] = Field(default_factory= lambda: next(c))
    nome : str
    idade : int
    
class Lista_Pessoas(BaseModel):
    pessoas: list[PessoaModelo]
    count: int
    
    