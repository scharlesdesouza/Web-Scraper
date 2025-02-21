import sqlite3
import requests
from bs4 import BeautifulSoup

def buscar_produtos(termo):
    termo_formatado = termo.replace(" ", "+")  # Substituir espaços por "+"
    url = f"https://www.lojamaeto.com/search/?q={termo_formatado}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar a página de pesquisa.")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    produtos = soup.find_all("div", class_="product")  # Ajuste conforme a estrutura do site
    
    lista_produtos = []
    for produto in produtos:
        sku = produto.get("data-sku")
        titulo_elem = produto.find("h4", class_="product-list-name")
        preco_elem = produto.find("span", class_="to-price")

        if not sku or not titulo_elem or not preco_elem:
            continue  # Ignorar caso falte alguma informação essencial

        titulo = titulo_elem.text.strip()
        preco = float(preco_elem.text.replace("R$", "").replace(",", "."))
        
        preco_pix_elem = produto.find("div", class_="cash-payment-container")
        preco_pix = float(preco_pix_elem.find("span", class_="to-price").text.replace("R$", "").replace(",", ".")) if preco_pix_elem else preco
        
        parcela_elem = produto.find("span", class_="installments-number")
        numero_parcelas = int(parcela_elem.text.replace("x", "")) if parcela_elem else 1
        
        valor_parcela_elem = produto.find("span", class_="installments-amount")
        valor_parcela = float(valor_parcela_elem.text.replace("R$", "").replace(",", ".")) if valor_parcela_elem else preco
        
        lista_produtos.append((sku, titulo, preco, preco_pix, valor_parcela, numero_parcelas))
    
    return lista_produtos

def salvar_no_banco(produtos):
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    
    for produto in produtos:
        cursor.execute('''
            INSERT INTO produtos (sku, titulo, preco, preco_pix, valor_parcela, numero_parcelas)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(sku) DO UPDATE SET
                titulo=excluded.titulo,
                preco=excluded.preco,
                preco_pix=excluded.preco_pix,
                valor_parcela=excluded.valor_parcela,
                numero_parcelas=excluded.numero_parcelas;
        ''', produto)
    
    conn.commit()
    conn.close()

def main():
    termo = input("Digite o nome do produto para buscar: ")
    produtos = buscar_produtos(termo)
    if produtos:
        salvar_no_banco(produtos)
        print(f"{len(produtos)} produtos salvos/atualizados no banco de dados.")
    else:
        print("Nenhum produto encontrado.")

if __name__ == "__main__":
    main()
