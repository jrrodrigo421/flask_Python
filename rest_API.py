from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            desenvolvedor = devs[id]
        except IndexError:
            desenvolvedor = {'status':'Erro', 'mensagem:':'Dev de ID {} nao existe!'.format(id)}
        except Exception:
            desenvolvedor = {'status:':'ERRO', 'mensagem':'Procure o ADM da API'}
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status:':'Sucesso','mensagem':'Registro Excluido'})

@app.route('/dev/', methods=['GET', 'POST'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)

