import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "qualquer_coisa_secreta"

produtos = {
    "Calça": [
        {"nome": "CALÇA BIA OFF", "preco": 132.08},
        {"nome": "CALÇA BIA CARAMELO", "preco": 132.08},
        {"nome": "CALÇA BIA VERSALE PRETO E BRANCO", "preco": 97.82},
    ],
    "Saia": [
        {"nome": "SAIA TRICO BRANCO", "preco": 92.18},
        {"nome": "SAIA TRICO NUDE", "preco": 0.00},
        {"nome": "SAIA GRINGA AZUL", "preco": 0.00},
        {"nome": "SAIA TULE AZUL BEBE", "preco": 0.00},
        {"nome": "SAIA TULE PRETO", "preco": 0.00},
        {"nome": "SAIA TEREZA MARROM C BRANCO", "preco": 0.00},
        {"nome": "SAIA TEREZA FERRUGO C BRANCO", "preco": 0.00},
        {"nome": "SAIA ELO OFF", "preco": 0.00},
        {"nome": "SAIA ELO MARROM", "preco": 0.00},
        {"nome": "SAIA LANA MARROM", "preco": 0.00},
        {"nome": "SAIA DARA MARROM", "preco": 0.00},
        {"nome": "SAIA DARA CAFE C LEITE", "preco": 0.00},
        {"nome": "SAIA DARA OFF", "preco": 0.00},
    ],
    "Chemise": [
        {"nome": "CHEMISE AZUL C BRANCO", "preco": 0.00},
        {"nome": "CHEMISE BRANCO C AMARELO", "preco": 0.00},
        {"nome": "CHEMISE BRANCO C NUDE", "preco": 0.00},
    ],
    "Vestido": [
        {"nome": "VESTIDO NO LARANJA", "preco": 0.00},
    ],
    "CJ": [
        {"nome": "CJ TALIA", "preco": 0.00},
    ],
    "Biquíni": [
        {"nome": nome, "preco": 0.00} for nome in [
            "BIQUINI GABI ONCINHA M", "BIQUINI GABI ONCINHA G", "BIQUINI GABI VERMELHO G",
            "BIQUINI GABI ROXO M", "BIQUINI GABI LARANJA G", "BIQUINI GABI PRETO G",
            "BIQUINI GABI MARROM M", "BIQUINI GABI VERDE P", "BIQUINI SOLAR AZUL BEBE G",
            "BIQUINI DEBORA ROSA M", "BIQUINI MELISSA MARROM M", "BIQUINI TALIA VERDE G",
            "BIQUINI TALIA VERMELHO G", "BIQUINI MARINA SOL AZUL G", "BIQUINI YOLANDA ROSE P",
            "BIQUINI JULIA BRANCO G", "BIQUINI ANTONELA VERDE LOURO M", "BIQUINI ESTELA AZUL MOSCOW G",
            "BIQUINI MARINA ROSA VERDE COLLOR M", "BIQUINI MARINA LARANJA C AZUL M", "MAIO BARRAMAS VERDE M",
            "MAIO ANITTA AZUL P", "MAIO ANITTA NUDE P", "BIQUINI LUMA VERDE P", "BIQUINI BELLE ROSA G",
            "BIQUINI CORAÇAO ROSA G", "BIQUINI NATALIA AZUL M", "BIQUINI NATALIA NUDE M",
            "BIQUINI SAMLA LARANJA P", "BIQUINI SAMLA LARANJA G", "BIQUINI SAMLA VERDE LOURO P",
            "BIQUINI SAMLA VERDE LOURO M", "BIQUINI SAMLA VERDE LOURO G", "BIQUINI SOFIA VINHO P",
            "BIQUINI SAMIA VINHO M", "BIQUINI SAMIA VINHO P", "BIQUINI SAMIA PRETO P",
            "BIQUINI RAYLINE NUDE P", "BIQUINI DAY NUDE M", "BIQUINI DAY NUDE P",
            "BIQUINI DAY VERDE MILITAR G", "BIQUINI DAY ROSA G", "BIQUINI DORY CINZA G",
            "BIQUINI FITA SUPLEX LARANJA U", "BIQUINI VERANO PRETO M", "BIQUINI VERANO MARROM G",
            "BIQUINI VERANO VINHO G", "BIQUINI SANTORINI P/B P", "BIQUINI SANTORINI P/B M",
            "BIQUINI SANTORINI P/B G", "BIQUINI LOUISIANA MARROM P", "BIQUINI SIRIOS BRONZE G"
        ]
    ],
    "Body": [
        {"nome": "BODY SIRIOS BRONZE M", "preco": 0.00},
        {"nome": "BODY MALU PRETO G", "preco": 0.00},
        {"nome": "BODY MALU VINHO G", "preco": 0.00},
    ],
    "Bolsa": [
        {"nome": "BOLSA PALHA SOL E MAR", "preco": 0.00},
        {"nome": "BOLSA BAU VERDE", "preco": 0.00},
        {"nome": "BOLSA CROCHE NUDE", "preco": 0.00},
    ],
    "Brinco": [
        {"nome": "BRINCO FLOR NUDE", "preco": 0.00},
        {"nome": "BRINCO FLOR VERDE", "preco": 0.00},
        {"nome": "BRINCO CETIM ROSA", "preco": 0.00},
        {"nome": "BRINCO FLOR AZUL", "preco": 0.00},
        {"nome": "BRINCO BUZIOS", "preco": 0.00},
    ],
    "Colar": [
        {"nome": "COLAR CONCHA BRANCO", "preco": 0.00},
        {"nome": "COLAR CONCHA DOURADO", "preco": 0.00},
    ]
}

@app.route("/")
def home():
    categoria = request.args.get("categoria", "Biquíni")
    produtos_cat = produtos.get(categoria, [])
    categorias = list(produtos.keys())
    qtd_carrinho = len(session.get("carrinho", []))
    return render_template("index.html", categorias=categorias, produtos=produtos_cat, categoria_atual=categoria, qtd_carrinho=qtd_carrinho)

@app.route("/add/<categoria>/<nome>")
def add_to_cart(categoria, nome):
    produto = next((p for p in produtos.get(categoria, []) if p["nome"] == nome), None)
    if not produto:
        flash("Produto não encontrado.")
        return redirect(url_for("home"))

    if "carrinho" not in session:
        session["carrinho"] = []

    session["carrinho"].append({"nome": produto["nome"], "preco": produto["preco"]})
    session.modified = True

    flash(f"{produto['nome']} adicionado ao carrinho!")
    return redirect(url_for("home", categoria=categoria))

@app.route("/carrinho")
def ver_carrinho():
    carrinho = session.get("carrinho", [])
    total = sum(item["preco"] for item in carrinho)
    return render_template("carrinho.html", carrinho=carrinho, total=total)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
