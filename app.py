from flask import Flask, render_template

app = Flask(__name__)

produtos = [
    {"nome": "CALÇA BIA OFF", "preco": 132.08},
    {"nome": "CALÇA BIA CARAMELO", "preco": 132.08},
    {"nome": "CALÇA BIA VERSALE PRETO E BRANCO", "preco": 97.82},
    {"nome": "SAIA TRICO BRANCO", "preco": 92.18},
    # ... (só continuar com todos os seus produtos)
]

@app.route("/")
def home():
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
