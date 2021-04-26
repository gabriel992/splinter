from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

#MENSAGEM NO MURAL
mural_mensagem = [
    {'pergunta':'Como tem sido seu homeoffice ?',
     'Mensagem': 'Seu feedback é importante para gente :)'  
    }
]    


mensagem = [
            {'id':0,'nome':'Gabriel','mensagem':'tem sido um desafio'},
            {'id':1,'nome':'Emerson','mensagem':'To de boa'},
            {'id':2,'nome':'Rodolfo','mensagem':'Tudo ok'}
]

#ROTA PARA POSTAR MENSAGENS 
@app.route("/colaborador/", methods=['POST','GET'])
def post_mensagem():
    if request.method == 'POST':
        try:
            dados       = json.loads(request.data)
            posicao     = len(mensagem)
            dados['id'] = posicao
            mensagem.append(dados)
            return jsonify({'Status':'Sucess','mensagem':'sua mensagem foi postada com sucesso!'})
        except Exception:
            mensagem_erro = 'Erro desconhecido'
            return jsonify(mensagem_erro)    

    elif request.method == 'GET':
        return jsonify (mural_mensagem, mensagem)

   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))    