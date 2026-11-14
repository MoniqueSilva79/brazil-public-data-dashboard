# 🇧🇷 Dashboard de Dados Públicos do Brasil

Dashboard interativo com dados públicos brasileiros: **população estimada por estado (IBGE)**, com filtros por região, ranking e gráficos.

## 🎯 Objetivo
Praticar *storytelling* com dados: transformar uma tabela pública em uma visão que qualquer pessoa entende em segundos.

## 📊 O que o dashboard mostra
- KPIs: população total, estado mais populoso, número de estados filtrados
- Ranking de estados (barras horizontais)
- Participação de cada região (gráfico de pizza)
- Tabela completa com download em CSV

## 🧰 Tecnologias
- Python 3.10+
- Streamlit
- pandas
- Plotly Express

## 📂 Dados
`data/populacao_uf.csv` traz a **estimativa populacional por UF (IBGE, Censo 2022)**.
Fonte oficial: [IBGE – Censo 2022](https://censo2022.ibge.gov.br/panorama/).
Você pode trocar o arquivo por outros dados públicos, como os do [Portal Brasileiro de Dados Abertos](https://dados.gov.br/) ou do [DataSUS](https://datasus.saude.gov.br/).

## 🚀 Como rodar
```bash
git clone https://github.com/MoniqueSilva79/brazil-public-data-dashboard.git
cd brazil-public-data-dashboard
pip install -r requirements.txt
streamlit run dashboard.py
```

## 📚 O que pratiquei
- Leitura e agregação de dados com pandas
- Visualizações interativas com Plotly
- Construção de dashboards com filtros

## 🗺️ Próximos passos
- [ ] Mapa coroplético por estado
- [ ] Buscar os dados direto da API do IBGE (SIDRA)
- [ ] Publicar no Streamlit Community Cloud
