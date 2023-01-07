from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from tinydb import TinyDB, Query


server = Flask(__name__) #Meu server (aplicativo) e ela vai usar o Flask
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)
database = TinyDB('database.json')

class Pessoa(BaseModel):
    id: Optional[int]
    idade: int
    nome: str

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int

@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def buscar_pessoa():
    """Retorna todas as pessoas da base de dados"""
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )

@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoa():
    """Insere uma pessoa no banco de dados"""
    body = request.get_json()
    database.insert(body)
    return body

@server.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def alterar_pessoa(id):
    """Altera uma pessoa no banco de dados a partir do id"""
    Pessoa = Query()
    body = request.get_json()
    database.update(body, Pessoa.id == id)
    return jsonify(body)

@server.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def excluir_pessoa(id):
    """Exclui uma pessoa no banco de dados a partir do id"""
    Pessoa = Query()
    database.remove(Pessoa.id == id)
    return jsonify({})

server.run()
