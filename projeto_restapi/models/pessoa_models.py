from pydantic import BaseModel

class PessoaModelo(BaseModel):
    id: int
    nome : str
    idade : int