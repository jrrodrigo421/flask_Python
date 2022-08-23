from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
devs = [

    {'id': '0',
    'nome':'Rodrigo',
    'Habilidades':['Python', 'Flask']
    },
    {'id':'1',
    'nome':'Lopes',
    'Habilidades':['Python', 'Django']
    }
]
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            desenvolvedor = devs[id]
        except IndexError:
            desenvolvedor = {'status':'Erro', 'mensagem:':'Dev de ID {} nao existe!'.format(id)}
        except Exception:
            desenvolvedor = {'status:':'ERRO', 'mensagem':'Procure o ADM da API'}
        return desenvolvedor

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        # return dados
        return{'status:': 'Sucesso', 'mensagem': 'Dados Alterados!'}

    def delete(self, id):
        devs.pop(id)
        return{'status:':'Sucesso','mensagem':'Registro Excluido'}
class ListaDevs(Resource):
    def get(self):
        return devs
    def post(self,):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDevs, '/dev/')
if __name__ == '__main__':  
    app.run(debug=True)