# Site Vitrine de Artes

Site vitrine desenvolvido em **Python com Flask** para exposição de artes autorais, prints e camisetas.

O objetivo do projeto é apresentar os produtos de forma profissional, sem realizar transações diretamente no site. As compras, dúvidas, disponibilidade, pagamento e envio são tratados diretamente pelo WhatsApp ou Instagram.

---

## Objetivo

Criar uma vitrine online simples, segura e fácil de manter, onde os visitantes possam:

- conhecer as artes disponíveis;
- visualizar prints e camisetas;
- acessar detalhes de cada produto;
- entrar em contato pelo WhatsApp com mensagem automática;
- acessar o Instagram do artista.

---

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- Jinja2
- Gunicorn
- Railway

---

## Estrutura do projeto

```txt
site-vitrine/
│
├─ main.py
├─ produtos.py
├─ requirements.txt
├─ Procfile
├─ README.md
│
├─ static/
│  ├─ css/
│  │  └─ style.css
│  └─ img/
│     └─ produto-exemplo.jpg
│
└─ templates/
   ├─ base.html
   ├─ index.html
   ├─ catalogo.html
   ├─ produto.html
   └─ sobre.html
```

---

## Funcionalidades

- Página inicial com apresentação da vitrine
- Catálogo de produtos
- Página individual para cada produto
- Botão de contato via WhatsApp
- Link para Instagram
- Produtos cadastrados diretamente no arquivo `produtos.py`
- Projeto sem banco de dados
- Projeto sem sistema de pagamento online
- Projeto sem login ou cadastro de usuário

---

## Como rodar o projeto localmente

### 1. Criar ambiente virtual

```bash
py -m venv .venv
```

### 2. Ativar ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o projeto

```bash
python main.py
```

Depois acesse no navegador:

```txt
http://127.0.0.1:5000
```

---

## Variáveis de ambiente

O projeto utiliza variáveis de ambiente para configurar os links de contato.

Exemplo:

```env
WHATSAPP_NUMERO=5585999999999
INSTAGRAM_URL=https://www.instagram.com/seuusuario
```

No Railway, essas variáveis devem ser cadastradas na aba de variáveis do projeto.

---

## Cadastro de produtos

Os produtos são cadastrados no arquivo `produtos.py`.

Exemplo:

```python
produtos = [
    {
        "id": 1,
        "slug": "camiseta-olho-cosmico",
        "nome": "Camiseta Olho Cósmico",
        "categoria": "Camiseta",
        "preco": "R$ 89,90",
        "imagem": "img/produto-exemplo.jpg",
        "descricao": "Camiseta com arte autoral em estilo surrealista.",
        "tamanhos": ["P", "M", "G", "GG"],
        "status": "Disponível"
    }
]
```

---

## Deploy

O projeto foi preparado para deploy no Railway.

O arquivo `Procfile` contém o comando de inicialização:

```txt
web: gunicorn main:app
```

As dependências necessárias estão no arquivo `requirements.txt`.

---

## Observação sobre vendas

Este site não realiza vendas diretamente.

Ele funciona apenas como uma vitrine dos produtos. Todo o processo de compra, pagamento, disponibilidade e envio é combinado diretamente entre o artista e o cliente por WhatsApp ou Instagram.

---

## Status do projeto

Em desenvolvimento.