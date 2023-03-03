from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    nome: str
    aulas: str
    horas: int
    instrutor: str

    @validator('nome')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras)<3:
            raise ValueError('Título precisa ter ao menos 3 palavras...')
        return value

