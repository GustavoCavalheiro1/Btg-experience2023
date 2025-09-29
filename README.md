# Análise de Valuation e Macro: VALE S.A.

## Relatório Executivo - Alfa Value

Este projeto apresenta uma análise de valuation e macroeconômica detalhada da VALE S.A., com foco em projeções de fluxo de caixa e indicadores-chave. O objetivo é fornecer uma visão abrangente da saúde financeira da empresa e suas perspectivas futuras, utilizando dados financeiros e análises de mercado.

### Autor

Gustavo Idalino Venceslau Cavalheiro

**Contato:** +5511962320573 | **Email:** gustavovences01@gmail.com

### Tese Principal

A VALE apresenta indicadores de _valuation_ que refletem um fluxo de caixa em recuperação. A diversificação de mercados e a resiliência do minério de ferro são fatores-chave para uma visão **POSITIVA** de longo prazo.

## Como Executar o Projeto

Para replicar a análise e gerar os relatórios, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema. As dependências do projeto estão listadas no arquivo `requirements.txt`.

### 2. Instalação das Dependências

Navegue até o diretório do projeto e instale as bibliotecas necessárias usando `pip`:

```bash
pip install -r requirements.txt
```

### 3. Execução da Análise

Execute o script principal `relatorio_vale.py` para gerar o relatório completo, incluindo indicadores, tabelas de projeção e o gráfico de Geração de Caixa Operacional (GCO):

```bash
python3 relatorio_vale.py
```

Ao final da execução, serão gerados os seguintes arquivos:

*   `vale_gco_analysis.png`: Imagem do gráfico de Geração de Caixa Operacional.
*   `vale_projecoes.csv`: Arquivo CSV com os dados de projeção de fluxo de caixa.

## Resultados da Análise

### 1. Indicadores-Chave de Valuation

A tabela abaixo resume os principais indicadores de valuation da VALE S.A. e o preço-alvo estabelecido na análise:

| Indicador                       | Valor                 |
| :------------------------------ | :-------------------- |
| Preço Alvo VALE ON              | R$ 74,37              |
| EV/EBITDA Atual (Negociado)     | 3,46x                 |
| EBITDA (Estimado)               | R$ 1.937.000.000,00   |
| Produção Anual de Ferro (toneladas) | 315.000.000,00        |
| Cotação do Minério de Ferro por Tonelada | R$ 425,00             |
| Target Price Longo Prazo (Minério) | U$ 85,00 @ R$ 5,00    |

### 2. Projeções de Fluxo de Caixa

As projeções de fluxo de caixa para os próximos anos (9 meses) são apresentadas a seguir, com valores em R$ Milhões:

```
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
| Período   |   Lucro Líquido |   Geração de Caixa Operacional (GCO) |   Investimentos em Capital Fixo (Capex) |   Posição do Caixa Final |
+===========+=================+======================================+=========================================+================----------+
| 2022 (9M) |            86.4 |                                 85.1 |                                   -36.6 |                     -5.6 |
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
| 2023 (9M) |            -2.2 |                                 50.3 |                                   -41.6 |                     -2.9 |
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
| 2024 (9M) |            -2.6 |                                104.2 |                                   -15.4 |                    148.2 |
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
| 2025 (9M) |            -1.4 |                                 18.2 |                                   -18.8 |                    -11.3 |
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
| 2026 (9M) |            -1.5 |                                 18.0 |                                   -16.8 |                     -0.6 |
+-----------+-----------------+--------------------------------------+-----------------------------------------+--------------------------+
```

### 3. Geração de Caixa Operacional (GCO) Projetada

O gráfico abaixo ilustra a projeção da Geração de Caixa Operacional (GCO) da VALE S.A., destacando o salto projetado de R$ 50 bilhões em 2023 para R$ 104 bilhões em 2024.

![Gráfico de Geração de Caixa Operacional (GCO)](https://private-us-east-1.manuscdn.com/sessionFile/yVa19UZEjiUQUP3VPi0XRV/sandbox/x3FiOZWfn6RMGJEGFFkjd0-images_1759179063684_na1fn_L2hvbWUvdWJ1bnR1L2J0Z19leHBlcmllbmNlX2ltcHJvdmVkL3ZhbGVfZ2NvX2FuYWx5c2lz.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUveVZhMTlVWkVqaVVRVVAzVlBpMFhSVi9zYW5kYm94L3gzRmlPWldmbjZSTUdKRUdGRmtqZDAtaW1hZ2VzXzE3NTkxNzkwNjM2ODRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwySjBaMTlsZUhCbGNtbGxibU5sWDJsdGNISnZkbVZrTDNaaGJHVmZaMk52WDJGdVlXeDVjMmx6LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=dHxT9T2jeegfARuzkgbcpwIwdnvQCMqo8iA43cwCWsJV98C8pcOHrcqnYSD0m3V-A7Vv5PvSj8tnkxJ~U69epm9~lb~hOHs6nE~uaQJSK4itv0-gr5091SyueP7K9Znx0C3UC5qXdvGIpM0dZ6T5G2kIp0bBDgDsYRJL4OaO5mGqurdpj0WF8inxBYXnPo3apL7JiyTAz~HC4jKLQqcdhqVnW~OBBHYKBUFedMiRqtW8PL1LnO5Tbl~Y~J4cMP9fcLR~6uJTx47k9g4m-~UWuK055evLJpJ7ODc9s3sF1luHELHr5314Xuaa95yL5vlLv9DtMu81TrCF0aaRmbEGLQ__)

### 4. Análise e Conclusões

#### 4.1. Destaques Macroeconômicos

O setor de mineração representa aproximadamente 4% do PIB brasileiro, com um faturamento de cerca de R$ 340 bilhões, e contribui com 30% das exportações nacionais (aproximadamente US$ 80 bilhões) [1].

**Riscos e Oportunidades:** Há sinais de recessão nas economias Americana e Chinesa, que podem impactar a demanda por minério de ferro. Além disso, o impacto do "imposto do pecado" na extração é um fator de risco [2]. Contudo, a VALE se beneficia de sua alta exposição cambial e da valorização do Dólar em suas receitas, apresentando uma oportunidade de crescimento.

#### 4.2. Análise Fundamentalista

*   **Caixa e Liquidez:** A Geração de Caixa Operacional (GCO) tem um salto projetado de R$ 50 bilhões (2023) para **R$ 104 bilhões (2024)**. O Capital de Giro negativo mantém expectativas de melhorias no fluxo de caixa.
*   **Despesas:** As maiores despesas da empresa ainda estão relacionadas aos processos de Brumadinho.
*   **Estratégia:** A VALE tem um movimento estratégico para diminuir sua exposição à China, focando em acordos com o Oriente Médio, Ásia e Europa, buscando diversificação geográfica.

#### 4.3. Fatores ESG e Recomendação

*   **Fatores ESG:** A VALE investe fortemente em tecnologias para neutralizar emissões de carbono e adota biocombustíveis e máquinas sustentáveis, demonstrando compromisso com a sustentabilidade.
*   **Recomendação:** O preço alvo de **R$ 74,37** é suportado pela resiliência do minério de ferro e pela estratégia de diversificação. A visão é **POSITIVA** de longo prazo.

## Referências

[1] [Setor de mineração no Brasil: dados e perspectivas](https://www.ibram.org.br/)
[2] [Impacto do imposto do pecado na mineração](https://www.gov.br/economia/pt-br/assuntos/noticias/2023/outubro/reforma-tributaria-imposto-seletivo-tera-aliquota-de-1-sobre-mineracao-e-petroleo-e-gas-e-nao-incidira-sobre-energia-eletrica-e-telecomunicacoes)

