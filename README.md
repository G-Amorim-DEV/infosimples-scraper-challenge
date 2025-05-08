
# 🦆 Infosimples - Desafio Técnico (Web Scraping)

Este repositório contém a solução para o desafio técnico proposto pela **Infosimples**, com foco na construção de um scraper web em **Python**.

## 📌 Sobre o Desafio

O objetivo do desafio era acessar uma página de produto de e-commerce fictícia e coletar automaticamente todas as suas informações relevantes. A página simulada foi:

🔗 https://infosimples.com/vagas/desafio/commercia/product.html

A tarefa consistia em:

- Acessar a página usando HTTP GET
- Fazer o parsing do HTML da página
- Extrair os seguintes dados:
  - Título do produto
  - Marca
  - Categorias
  - Descrição
  - Variações do produto (nome, preço atual, preço antigo e disponibilidade)
  - Propriedades técnicas do produto (ex: material, cor, peso, origem, etc.)
  - Avaliações de clientes (nome, data, nota e comentário)
  - Nota média das avaliações
  - URL da página

O resultado final deveria ser salvo em um arquivo `produto.json`, com todos os dados estruturados no formato solicitado.

## 📂 Arquivos no Repositório

- `Take_Home_Coding_Challenge.py`: Script Python responsável por acessar a página, extrair os dados e salvá-los em JSON.
- `produto.json`: Resultado da execução do scraper com os dados extraídos.

> ⚠️ O arquivo PDF original com a descrição do desafio **não será incluído** neste repositório, mas todas as informações relevantes foram descritas aqui.

## 🧰 Tecnologias Utilizadas

- Python 3
- BeautifulSoup4
- Requests
- JSON

## ▶️ Como Executar

1. Instale as dependências:

```bash
pip install requests beautifulsoup4
```

2. Execute o script:

```bash
python Take_Home_Coding_Challenge.py
```

3. O arquivo `produto.json` será gerado com os dados extraídos da página.

---

# 🦆 Infosimples - Take-Home Coding Challenge (Web Scraping)

This repository contains the solution to the take-home coding challenge proposed by **Infosimples**, focusing on building a **Python** web scraper.

## 📌 About the Challenge

The goal of the challenge was to automatically access and extract structured data from a simulated e-commerce product page:

🔗 https://infosimples.com/vagas/desafio/commercia/product.html

The task included:

- Making an HTTP GET request to the page  
- Parsing the HTML content  
- Extracting the following information:
  - Product title
  - Brand
  - Categories
  - Description
  - Product variations (name, current price, old price, availability)
  - Product properties (e.g., material, color, weight, origin, etc.)
  - Customer reviews (name, date, score, and review text)
  - Average review score
  - Page URL

The extracted information was saved in a structured `produto.json` file.

## 📂 Files in the Repository

- `Take_Home_Coding_Challenge.py`: Python script that performs scraping and writes the data to JSON.
- `produto.json`: Final result containing the extracted product data.

> ⚠️ The original PDF with the full challenge description is **not included** in this repository. All relevant details have been explained here.

## 🧰 Technologies Used

- Python 3
- BeautifulSoup4
- Requests
- JSON

## ▶️ How to Run

1. Install the dependencies:

```bash
pip install requests beautifulsoup4
```

2. Run the script:

```bash
python Take_Home_Coding_Challenge.py
```

3. The `produto.json` file will be created with the extracted data.
