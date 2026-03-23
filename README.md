🏠Pipeline de dados completo sobre o mercado imobiliário brasileiro, cobrindo desde a ingestão dos dados brutos até análises via SQL.

## 📌 Sobre o projeto

Este projeto simula um pipeline ETL real, processando dados de **35.772 imóveis** para alugar no Brasil extraídos da plataforma ZAP Imóveis.

O pipeline passa por três etapas:
- **Ingestão** — leitura e carregamento do dataset bruto
- **Transformação** — limpeza, padronização e criação de métricas
- **Carregamento** — armazenamento em banco SQLite e análise via SQL

## 🛠️ Tecnologias

- Python 3.14
- Pandas
- SQLite3
- SQLAlchemy
- Git & GitHub

## 📁 Estrutura do projeto
```
pipeline-imoveis-br/
│
├── data/
│   ├── raw/          # dados originais
│   └── processed/    # dados tratados
│
├── src/
│   ├── ingestao.py
│   ├── transformacao.py
│   └── carregamento.py
│
├── database/         # banco SQLite gerado
├── main.py           # executa o pipeline completo
└── README.md
```

## ▶️ Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/Mateuzz-m/pipeline-imoveis-br.git
cd pipeline-imoveis-br
```

**2. Instale as dependências**
```bash
pip install pandas sqlalchemy openpyxl
```

**3. Adicione o dataset**

Baixe o dataset [Brazilian Real Estate to Rent](https://www.kaggle.com/datasets/maverickjpa/brazilian-real-estate-to-rent) e coloque o arquivo CSV em `data/raw/dataZAP.csv`

**4. Execute o pipeline**
```bash
python main.py
```

## 📊 Resultados

Após o pipeline, **23.966 imóveis** foram processados e carregados no banco com as seguintes análises:

- Preço médio de aluguel por estado
- Top 5 bairros mais caros por m² em São Paulo
- Distribuição de imóveis por tipo

