import os
from urllib.parse import quote

from dotenv import load_dotenv
from flask import Flask, render_template, abort

from produtos import produtos


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-local-de-desenvolvimento")


WHATSAPP_NUMERO = os.getenv("WHATSAPP_NUMERO", "5500000000000")
INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "#")
NOME_SITE = os.getenv("NOME_SITE", "Site Vitrine")


@app.context_processor
def variaveis_globais():
    return {
        "nome_site": NOME_SITE,
        "instagram_url": INSTAGRAM_URL
    }


@app.route("/")
def index():
    produtos_destaque = produtos[:3]

    return render_template(
        "index.html",
        produtos_destaque=produtos_destaque
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        produtos=produtos
    )


@app.route("/produto/<slug>")
def detalhe_produto(slug):
    produto = next((item for item in produtos if item["slug"] == slug), None)

    if produto is None:
        abort(404)

    mensagem = (
        f"Oi! Tenho interesse no produto: {produto['nome']}. "
        "Poderia me passar mais informações?"
    )

    link_whatsapp = f"https://wa.me/{WHATSAPP_NUMERO}?text={quote(mensagem)}"

    return render_template(
        "produto.html",
        produto=produto,
        link_whatsapp=link_whatsapp
    )


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)