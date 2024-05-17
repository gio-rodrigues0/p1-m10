from flask import Flask
from database.database import db
from flask import jsonify, request
from database.models import Pedidos

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

# Verifica se o parâmetro create_db foi passado na linha de comando
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    # cria o banco de dados
    with app.app_context():
        db.create_all()
    # Finaliza a execução do programa
    print("Database created successfully")
    sys.exit(0)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Adicionando as rotas CRUD para a entidade Pedidos
@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    pedidos = Pedidos.query.all()
    return_pedidos = []
    for pedido in pedidos:
        return_pedidos.append(pedido.serialize())
    return jsonify(return_pedidos)

@app.route("/pedidos/<int:id>", methods=["GET"])
def get_pedido(id):
    pedido = Pedidos.query.get(id)

    if pedido is None:
        return jsonify({"msg": "Pedido não encontrado"}), 404
    
    return jsonify(pedido.serialize())

@app.route("/pedidos", methods=["POST"])
def create_pedido():
    data = request.json
    pedido = Pedidos(name=data["name"], email=data["email"], description=data["description"])
    db.session.add(pedido)
    db.session.commit()
    return jsonify(pedido.serialize())

@app.route("/pedidos/<int:id>", methods=["PUT"])
def update_pedido(id):
    data = request.json
    pedido = Pedidos.query.get(id)
    pedido.name = data["name"]
    pedido.email = data["email"]
    pedido.description = data["description"]
    db.session.commit()
    return jsonify(pedido.serialize())

@app.route("/pedidos/<int:id>", methods=["DELETE"])
def delete_pedido(id):
    pedido = Pedidos.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'msg': 'Pedido deletado com sucesso!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 