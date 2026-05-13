import os
from urllib.parse import quote

from Flask import Flask, render_template, abort

from produtos import produtos


app = Flask(__name__)


WHATSAPP_NUMERO = os.getenv("WHATSAPP_NUMERO", "5585999999999")
INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "https://www.instagram.com/seuusuario")


@app.route("/")
def index():
    produtos_destaque = produtos[:3]

    return render_template(
        "index.html",
        produtos_destaque=produtos_destaque,
        instagram_url=INSTAGRAM_URL
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        produtos=produtos,
        instagram_url=INSTAGRAM_URL
    )


@app.route("/produto/<slug>")
def detalhe_produto(slug):
    produto = next((item for item in produtos if item["slug"] == slug), None)

    if produto is None:
        abort(404)

    mensagem = f"Oi! Tenho interesse no produto: {produto['nome']}. Poderia me passar mais informações?"
    link_whatsapp = f"https://wa.me/{WHATSAPP_NUMERO}?text={quote(mensagem)}"

    return render_template(
        "produto.html",
        produto=produto,
        link_whatsapp=link_whatsapp,
        instagram_url=INSTAGRAM_URL
    )


@app.route("/sobre")
def sobre():
    return render_template(
        "sobre.html",
        instagram_url=INSTAGRAM_URL
    )


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("base.html", erro_404=True), 404


if __name__ == "__main__":
    app.run(debug=True)