from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from tinydb import TinyDB, Query


server = Flask(__name__) #Meu server (aplicativo) e ela vai usar o Flask
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)
database = TinyDB('database.json')


class Pessoa(BaseModel):
    id: int
    idade: int
    nome: str


@server.get('/pessoas')
def buscar_pessoa():
    """Retorna todas as pessoas da base de dados"""
    return database.all()


@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoa():
    """Insere uma pessoa no banco de dados"""
    body = request.get_json()
    database.insert(body)
    return body


server.run()
