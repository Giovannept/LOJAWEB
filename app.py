from flask import Flask, render_template, request

app = Flask(__name__)

produtos = {
    "Calça": [
        {"nome": "CALÇA BIA OFF", "preco": 0.00},
        {"nome": "CALÇA BIA CARAMELO", "preco": 0.00},
        {"nome": "CALÇA BIA VERSALE PRETO E BRANCO", "preco": 0.00},
    ],
    "Saia": [
        {"nome": "SAIA TRICO BRANCO", "preco": 0.00},
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
        {"nome": "BIQUINI GABI ONCINHA M", "preco": 0.00},
        {"nome": "BIQUINI GABI ONCINHA G", "preco": 0.00},
        {"nome": "BIQUINI GABI VERMELHO G", "preco": 0.00},
        {"nome": "BIQUINI GABI ROXO M", "preco": 0.00},
        {"nome": "BIQUINI GABI LARANJA G", "preco": 0.00},
        {"nome": "BIQUINI GABI PRETO G", "preco": 0.00},
        {"nome": "BIQUINI GABI MARROM M", "preco": 0.00},
        {"nome": "BIQUINI GABI VERDE P", "preco": 0.00},
        {"nome": "BIQUINI SOLAR AZUL BEBE G", "preco": 0.00},
        {"nome": "BIQUINI DEBORA ROSA M", "preco": 0.00},
        {"nome": "BIQUINI MELISSA MARROM M", "preco": 0.00},
        {"nome": "BIQUINI TALIA VERDE G", "preco": 0.00},
        {"nome": "BIQUINI TALIA VERMELHO G", "preco": 0.00},
        {"nome": "BIQUINI MARINA SOL AZUL G", "preco": 0.00},
        {"nome": "BIQUINI YOLANDA ROSE P", "preco": 0.00},
        {"nome": "BIQUINI JULIA BRANCO G", "preco": 0.00},
        {"nome": "BIQUINI ANTONELA VERDE LOURO M", "preco": 0.00},
        {"nome": "BIQUINI ESTELA AZUL MOSCOW G", "preco": 0.00},
        {"nome": "BIQUINI MARINA ROSA VERDE COLLOR M", "preco": 0.00},
        {"nome": "BIQUINI MARINA LARANJA C AZUL M", "preco": 0.00},
        {"nome": "MAIO BARRAMAS VERDE M", "preco": 0.00},
        {"nome": "MAIO ANITTA AZUL P", "preco": 0.00},
        {"nome": "MAIO ANITTA NUDE P", "preco": 0.00},
        {"nome": "BIQUINI LUMA VERDE P", "preco": 0.00},
        {"nome": "BIQUINI BELLE ROSA G", "preco": 0.00},
        {"nome": "BIQUINI CORAÇAO ROSA G", "preco": 0.00},
        {"nome": "BIQUINI NATALIA AZUL M", "preco": 0.00},
        {"nome": "BIQUINI NATALIA NUDE M", "preco": 0.00},
        {"nome": "BIQUINI SAMLA LARANJA P", "preco": 0.00},
        {"nome": "BIQUINI SAMLA LARANJA G", "preco": 0.00},
        {"nome": "BIQUINI SAMLA VERDE LOURO P", "preco": 0.00},
        {"nome": "BIQUINI SAMLA VERDE LOURO M", "preco": 0.00},
        {"nome": "BIQUINI SAMLA VERDE LOURO G", "preco": 0.00},
        {"nome": "BIQUINI SOFIA VINHO P", "preco": 0.00},
        {"nome": "BIQUINI SAMIA VINHO M", "preco": 0.00},
        {"nome": "BIQUINI SAMIA VINHO P", "preco": 0.00},
        {"nome": "BIQUINI SAMIA PRETO P", "preco": 0.00},
        {"nome": "BIQUINI RAYLINE NUDE P", "preco": 0.00},
        {"nome": "BIQUINI DAY NUDE M", "preco": 0.00},
        {"nome": "BIQUINI DAY NUDE P", "preco": 0.00},
        {"nome": "BIQUINI DAY VERDE MILITAR G", "preco": 0.00},
        {"nome": "BIQUINI DAY ROSA G", "preco": 0.00},
        {"nome": "BIQUINI DORY CINZA G", "preco": 0.00},
        {"nome": "BIQUINI FITA SUPLEX LARANJA U", "preco": 0.00},
        {"nome": "BIQUINI VERANO PRETO M", "preco": 0.00},
        {"nome": "BIQUINI VERANO MARROM G", "preco": 0.00},
        {"nome": "BIQUINI VERANO VINHO G", "preco": 0.00},
        {"nome": "BIQUINI SANTORINI P/B P", "preco": 0.00},
        {"nome": "BIQUINI SANTORINI P/B M", "preco": 0.00},
        {"nome": "BIQUINI SANTORINI P/B G", "preco": 0.00},
        {"nome": "BIQUINI LOUISIANA MARROM P", "preco": 0.00},
        {"nome": "BIQUINI SIRIOS BRONZE G", "preco": 0.00},
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
    return render_template("index.html", categorias=categorias, produtos=produtos_cat, categoria_atual=categoria)

if __name__ == "__main__":
    app.run(debug=True)
