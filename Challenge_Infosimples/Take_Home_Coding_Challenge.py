from bs4 import BeautifulSoup
import requests
import json

def extrair_texto(elem):
    return elem.get_text(strip=True) if elem else ""

def converter_preco(elem):
    if not elem:
        return None
    try:
        return float(elem.get_text(strip=True).replace("R$", "").replace(",", "."))
    except ValueError:
        return None

url = "https://infosimples.com/vagas/desafio/commercia/product.html"
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, "html.parser")

titulo = extrair_texto(html.select_one("h2#product_title"))
marca = extrair_texto(html.select_one(".brand"))
categorias = [a.get_text(strip=True) for a in html.select("nav.current-category a")]

descricao_elem = html.select("div.proddet p")
descricao = " ".join(p.get_text(strip=True) for p in descricao_elem) if descricao_elem else ""

skus = []
for item in html.select(".card-container"):
    nome = extrair_texto(item.select_one(".prod-nome"))
    preco_atual = converter_preco(item.select_one(".prod-pnow"))
    preco_antigo = converter_preco(item.select_one(".prod-pold"))

    skus.append({
        "name": nome,
        "current_price": preco_atual,
        "old_price": preco_antigo,
        "available": True
    })

def coletar_propriedades(tabela):
    propriedades = []
    for linha in tabela.select("tr"):
        colunas = linha.find_all("td")
        if len(colunas) == 2:
            propriedades.append({
                "label": colunas[0].get_text(strip=True),
                "value": colunas[1].get_text(strip=True)
            })
    return propriedades

properties = []

tabela_principal = html.select_one("div:has(h4:-soup-contains('Product properties')) table")
if tabela_principal:
    properties.extend(coletar_propriedades(tabela_principal))

tabela_adicional = html.select_one("#propadd table")
if tabela_adicional:
    properties.extend(coletar_propriedades(tabela_adicional))

avaliacoes = []
soma_notas = 0

for bloco in html.select("#comments .analisebox"):
    nome = extrair_texto(bloco.select_one(".analiseusername"))
    data = extrair_texto(bloco.select_one(".analisedate"))
    texto = extrair_texto(bloco.select_one("p"))
    estrelas = bloco.select_one(".analisestars")
    nota = estrelas.get_text(strip=True).count("★") if estrelas else 0

    soma_notas += nota

    avaliacoes.append({
        "name": nome,
        "date": data,
        "score": nota,
        "text": texto
    })

media_avaliacoes = round(soma_notas / len(avaliacoes), 2) if avaliacoes else 0.0

dados = {
    "title": titulo,
    "brand": marca,
    "categories": categorias,
    "description": descricao,
    "skus": skus,
    "properties": properties,
    "reviews": avaliacoes,
    "reviews_average_score": media_avaliacoes,
    "url": url
}


with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)

print("Arquivo 'produto.json' salvo com sucesso!")
