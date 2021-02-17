from flask import Flask, jsonify, request
import json
import math
app = Flask(__name__)


@app.route("/<int:id>")
def pessoa(id):
    return jsonify({'id': id, 'nome': 'Gabriel', 'profissao': 'Estudante'})


@app.route("/soma/<int:valor1>/<int:valor2>")
def soma(valor1, valor2):
    return {'soma': valor1 + valor2}


@app.route("/multi", methods=['POST', 'GET'])
def multi():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = math.prod(dados['valores'])
    elif request.method == 'GET':
        total = 10 * 10
    return jsonify({'Multiplicação': total})


if __name__ == '__main__':
    app.run(debug=True)
