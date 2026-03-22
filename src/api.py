from flask import Flask, request, jsonify
from src.calculator import calcular_preco

app = Flask(__name__)


@app.route("/calcular", methods=["GET"])
def calcular_endpoint():
    try:
        largura = float(request.args.get("largura", 0))
        altura = float(request.args.get("altura", 0))
        quantidade = int(request.args.get("quantidade", 1))
        tipo_papel = request.args.get("papel", "couche")

        preco = calcular_preco(largura, altura, quantidade, tipo_papel)
        return jsonify({"preco": preco}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run()
