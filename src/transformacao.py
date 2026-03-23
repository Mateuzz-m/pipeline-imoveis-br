import pandas as pd
import os

ARQUIVO_RAW = os.path.join("data", "raw", "dataZAP.csv")
ARQUIVO_PROCESSED = os.path.join("data", "processed", "imoveis_tratados.csv")

def transformar():
    print("Carregando dados brutos...")
    df = pd.read_csv(ARQUIVO_RAW, encoding='latin1', sep=';', low_memory=False)

    print("Selecionando colunas relevantes...")
    df = df[[
        'listing.address.city',
        'listing.address.state',
        'listing.address.neighborhood',
        'listing.address.zone',
        'listing.propertyType',
        'listing.bedrooms',
        'listing.bathrooms',
        'listing.parkingSpaces',
        'listing.usableAreas',
        'listing.pricingInfo.rentalPrice',
        'listing.pricingInfo.monthlyCondoFee',
        'listing.pricingInfo.yearlyIptu',
        'listing.furnished',
        'type'
    ]]

    print("Renomeando colunas...")
    df.columns = [
        'cidade', 'estado', 'bairro', 'zona',
        'tipo_imovel', 'quartos', 'banheiros',
        'vagas', 'area_m2', 'preco_aluguel',
        'condominio', 'iptu_anual', 'mobiliado', 'categoria'
    ]

    print("Corrigindo encoding...")
    for col in ['cidade', 'estado', 'bairro', 'zona', 'tipo_imovel']:
        df[col] = df[col].apply(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)

    print("Convertendo tipos numéricos...")
    for col in ['preco_aluguel', 'condominio', 'iptu_anual', 'area_m2']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    print("Removendo duplicatas...")
    df = df.drop_duplicates()

    print("Removendo linhas sem preço ou área...")
    df = df.dropna(subset=['preco_aluguel', 'area_m2'])

    print("Criando coluna preço por m²...")
    df['preco_por_m2'] = (df['preco_aluguel'] / df['area_m2']).round(2)

    print(f"\nDados tratados: {df.shape[0]} imóveis, {df.shape[1]} colunas")
    print(df.head())

    print("\nSalvando arquivo tratado...")
    df.to_csv(ARQUIVO_PROCESSED, index=False, encoding='utf-8-sig')
    print(f"Salvo em: {ARQUIVO_PROCESSED}")

    return df

if __name__ == "__main__":
    df = transformar()