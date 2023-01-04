from flask import Flask

server = Flask (__name__)

@server.get('/pessoas')
def pegar_pessoas():
    return 'Programaticamente Falando'

server.run()