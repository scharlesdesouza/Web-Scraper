# Web Scraper - Loja Maeto 🛒  

## 📌 Descrição  
Este projeto é um **Web Scraper** desenvolvido em Python que coleta informações de produtos de um site, armazena em um banco de dados SQLite e permite a leitura dos produtos salvos.

## 🚀 Funcionalidades  
- 🔍 **Busca de produtos**: pesquisa produtos no site com base em um termo de busca.  
- 📊 **Extração de dados**: coleta SKU, título, preço, preço no PIX, número de parcelas e valor da parcela.  
- 💾 **Armazenamento no banco SQLite**: salva as informações no banco de dados `produtos.db`.  
- 🔄 **Atualização de produtos**: se um produto já existe no banco, suas informações são atualizadas.  
- 📜 **Visualização de produtos**: permite listar os produtos armazenados no banco.  

## 🛠 Tecnologias Utilizadas  
- **Python 3**  
- **BeautifulSoup** (para extração de dados do HTML)  
- **SQLite3** (para armazenamento dos produtos)  
- **Requests** (para acessar o site)  

## 📂 Estrutura do Projeto  
```
web_scraper/
│── create_database.py   # Cria o banco de dados
│── web_scraping.py      # Faz a busca e armazena os produtos
│── read_products.py     # Exibe os produtos armazenados
│── README.md            # Documentação do projeto
│── .gitignore           # Evita o envio do banco de dados ao repositório
```

## 📋 Como Executar  
### 1 Clonar o Repositório
Clone este repositório em seu computador; 
### 2 Criar o Banco de Dados 
Execute primeiro o script que faz a criação do banco de dados;
### 3 Executar programa 
Execute o script principal: web_scraping;
### 4 Buscar Produtos e Armazenar no Banco de Dados
Digite o nome do produto quando solicitado e aguarde a coleta e armazenamento dos dados;
### 5 Visualizar os Produtos Salvos
execute o script read_products para visualizar os produtos salvos no banco de dados;


## 🛠 Estrutura da Tabela SQLite  
A tabela `produtos` possui os seguintes campos:  
- `sku` (TEXT, chave primária)  
- `titulo` (TEXT)  
- `preco` (REAL)  
- `preco_pix` (REAL)  
- `valor_parcela` (REAL)  
- `numero_parcelas` (INTEGER)  

## ⚠ Observações  
- O banco de dados **não** é enviado ao repositório (`produtos.db` está no `.gitignore`).  
---  
Projeto desenvolvido para fins de aprendizado e automação. Qualquer dúvida ou sugestão, sinta-se à vontade para contribuir! 🚀

