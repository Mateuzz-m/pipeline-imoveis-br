import pandas as pd
import sqlite3
import os

ARQUIVO_PROCESSED = os.path.join("data", "processed", "imoveis_tratados.csv")
BANCO = os.path.join("database", "imoveis.db")

def carregar():
    print("Lendo dados tratados...")
    df = pd.read_csv(ARQUIVO_PROCESSED, encoding='utf-8-sig')

    print("Conectando ao banco de dados...")
    conn = sqlite3.connect(BANCO)

    print("Carregando dados no banco...")
    df.to_sql("imoveis", conn, if_exists="replace", index=False)

    print("Verificando carga...")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM imoveis")
    total = cursor.fetchone()[0]
    print(f"Total de registros no banco: {total}")

    print("\nExemplo de queries SQL:")

    print("\n--- Preço médio de aluguel por estado ---")
    query1 = """
        SELECT estado, ROUND(AVG(preco_aluguel), 2) as preco_medio
        FROM imoveis
        GROUP BY estado
        ORDER BY preco_medio DESC
    """
    print(pd.read_sql(query1, conn).to_string(index=False))

    print("\n--- Top 5 bairros mais caros por m² em SP ---")
    query2 = """
        SELECT bairro, ROUND(AVG(preco_por_m2), 2) as media_preco_m2
        FROM imoveis
        WHERE estado = 'São Paulo' AND preco_por_m2 > 0
        GROUP BY bairro
        ORDER BY media_preco_m2 DESC
        LIMIT 5
    """
    print(pd.read_sql(query2, conn).to_string(index=False))

    print("\n--- Quantidade de imóveis por tipo ---")
    query3 = """
        SELECT tipo_imovel, COUNT(*) as quantidade
        FROM imoveis
        GROUP BY tipo_imovel
        ORDER BY quantidade DESC
    """
    print(pd.read_sql(query3, conn).to_string(index=False))

    conn.close()
    print("\nBanco de dados criado com sucesso!")

if __name__ == "__main__":
    carregar()