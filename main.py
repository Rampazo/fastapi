from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class PessoaRequest(BaseModel):
    nome: str = Field(..., example="João")
    idade: int = Field(..., ge=0, example=20)


@app.get("/")
def home():
    return {"message": "Hello TutLinks.com"}


@app.post("/verificar-idade")
def verificar_idade(pessoa: PessoaRequest):
    if pessoa.idade >= 65:
        classificacao = "idosa"
    elif pessoa.idade >= 18:
        classificacao = "maior de idade"
    else:
        classificacao = "menor de idade"

    return {
        "nome": pessoa.nome,
        "idade": pessoa.idade,
        "classificacao": classificacao,
    }
