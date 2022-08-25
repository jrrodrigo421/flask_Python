from models import *

def insere_pessoas():
    pessoa = Pessoas(nome='Rodrigo', idade=29)
    # print(pessoa)
    # db_session.add(pessoa)
    # db_session.commit
    
    pessoa.save()
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # for i in pessoa:
    #     print(i.nome)
    # pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    # print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='JUNIOR').first()
    pessoa.delete()

if __name__ =='__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()

