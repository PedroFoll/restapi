from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response
from models import pessoa_models

pessoa = pessoa_models.PessoaModelo

server = Flask (__name__)
spec = FlaskPydanticSpec('flask', title='Aula de Api')
spec.register(server)

@server.get('/pessoas') # Rota, endpoint, recurso
@spec.validate(resp=Response(HTTP_200=pessoa))
def pegar_pessoas():
    return 'Programaticamente Falando'

server.run()

