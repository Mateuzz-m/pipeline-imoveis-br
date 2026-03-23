import pandas as pd
import os

ARQUIVO = os.path.join("data", "raw", "dataZAP.csv")

def carregar_dados():
    print("Carregando dados...")
    df = pd.read_csv(ARQUIVO, encoding='latin1', sep=';', low_memory=False)
    
    print(f"Total de imóveis: {df.shape[0]}")
    print(f"Total de colunas: {df.shape[1]}")
    print(f"\nColunas disponíveis:\n{list(df.columns)}")
    print(f"\nPrimeiras linhas:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    df = carregar_dados()