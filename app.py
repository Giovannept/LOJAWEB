from flask import Flask, render_template, request

app = Flask(__name__)

produtos = {
    "Biquíni": [
        {"nome": "Biquíni Estampado", "preco": 79.90},
        {"nome": "Biquíni Preto", "preco": 89.90},
    ],
    "Saia": [
        {"nome": "Saia Jeans", "preco": 120.00},
        {"nome": "Saia Tricô", "preco": 92.18},
    ],
    "Calça": [
        {"nome": "Calça Bia Off", "preco": 132.08},
        {"nome": "Calça Bia Caramelo", "preco": 132.08},
    ]
}

@app.route("/")
def home():
    categoria = request.args.get("categoria", "Biquíni")
    produtos_cat = produtos.get(categoria, [])
    categorias = list(produtos.keys())
    return render_template("index.html", categorias=categorias, produtos=produtos_cat, categoria_atual=categoria)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
