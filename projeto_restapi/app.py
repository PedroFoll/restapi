from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from models import pessoa_models
from tinydb import TinyDB , Query

pessoa = pessoa_models.PessoaModelo
lista_pessoas=pessoa_models.Lista_Pessoas
database = TinyDB('database.json')
server = Flask (__name__)
spec = FlaskPydanticSpec('flask', title='Aula de Api')
spec.register(server)

@server.get('/pessoas') # Rota, endpoint, recurso
@spec.validate(resp=Response(HTTP_200=lista_pessoas))
def buscar_pessoas():
    """Retorna todas as pessoas do Banco de Dados"""
    return jsonify(
        lista_pessoas(pessoas=database.all(),
                      count=len(database.all())
                      ).dict()
    )
    

@server.post('/pessoas')
@spec.validate(body=Request(pessoa), resp=Response(HTTP_200=pessoa))
def inserir_pessoas():
    """INSERE UMA PESSOA NO BANCO DE DADOS"""
    body = request.context.body.dict()
    database.insert(body)
    return body

@server.put('/pessoas/<int:id>')
@spec.validate(
    body=Request(pessoa), resp=Response(HTTP_200=pessoa)
)
def altera_pessoa(id):
    pessoa_models = Query() #Query para alteração, informando onde será feita a alteração
    body = request.context.body.dict() #Informa onde, dentro da classe, que será feita e a alteração.
    database.update(body, pessoa_models.id == id) # Informa que será mudado o corpo da documentação (body), onde o dentro do modelo de pessoas o ID for igual ao informado (pessoas_model.id == id)
    return jsonify(body)# Retorna a lista já com a alteração feita.
    
@server.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204')
)
def deleta_pessoa(id):
    pessoa_models = Query() #Query para alteração, informando onde será feita a alteração
    database.remove(pessoa_models.id == id) # Informa que será mudado o corpo da documentação (body), onde o dentro do modelo de pessoas o ID for igual ao informado (pessoas_model.id == id)
    return jsonify({})# Retorna a lista já com a alteração feita.

server.run()

