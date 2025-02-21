import sqlite3

def ver_produtos():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    if not produtos:
        print("Nenhum produto encontrado no banco de dados.")
    else:
        print("\nLista de produtos salvos:")
        print("-" * 80)
        for produto in produtos:
            print(f"SKU: {produto[0]}")
            print(f"Título: {produto[1]}")
            print(f"Preço: R$ {produto[2]:.2f}")
            print(f"Preço no PIX: R$ {produto[3]:.2f}")
            print(f"Valor da Parcela: R$ {produto[4]:.2f} em {produto[5]}x")
            print("-" * 80)
    
    conn.close()

if __name__ == "__main__":
    ver_produtos()
