from src.ingestao import carregar_dados
from src.transformacao import transformar
from src.carregamento import carregar

if __name__ == "__main__":
    print("=" * 40)
    print("PIPELINE IMÓVEIS BR")
    print("=" * 40)

    print("\n[1/3] INGESTÃO")
    carregar_dados()

    print("\n[2/3] TRANSFORMAÇÃO")
    transformar()

    print("\n[3/3] CARREGAMENTO")
    carregar()

    print("\n" + "=" * 40)
    print("Pipeline finalizado com sucesso!")
    print("=" * 40)