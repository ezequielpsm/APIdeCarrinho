from flask import Flask, jsonify, request 

app = Flask (__name__)

produtos = [
    {
        'id': 1,
        'titulo': 'Titlulo',
        'autor': '111'
    },

    {
        'id': 2,
        'titulo': 'hahahah',
        'autor': '222'
    },

    {
        'id': 3,
        'titulo': 'kkkkkk',
        'autor': '333'
    },
]

# Consultar todos
@app.route('/produtos',methods=['GET'])
def obter():
    return jsonify(produtos)

#Consultar(id)
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_por_id(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)

#Editar
@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_por_id(id):
    produto_alterado = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])
         
#Criar 
@app.route('/produtos', methods=['POST'])
def incluir_novo_produto():

    novo_produto = request.get_json()
    produtos.append(novo_produto)    

    return jsonify(produtos)


#Excluir
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_por_id(id):
    for indice,produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)

app.run(port=5000, host='localhost', debug=True)

