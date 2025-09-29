# Relatório de Valuation e Macro: VALE S.A. (Alfa Value)

## 🎯 Resumo Executivo e Recomendação

Este projeto em Python gera um relatório completo de Valuation e Análise Macroeconômica da Vale S.A., apresentando **indicadores-chave, projeções de fluxo de caixa e análise qualitativa**.

| Indicador Chave | Valor | Conclusão |
| :--- | :--- | :--- |
| **Preço Alvo VALE ON** | **R$ 74,37** | **Recomendação POSITIVA** de longo prazo. |
| **Geração de Caixa Operacional (GCO) Proj. 2024 (9M)** | **R$ 104,1 Bilhões** | Forte recuperação do fluxo de caixa, dobrando o valor de 2023. |
| **Estratégia** | Diversificação | Redução da exposição à China e foco em mercados desenvolvidos (Oriente Médio, Europa). |

---

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# --- 1. DADOS DE VALUATION (VALE S.A.) ---

# A. Indicadores-Chave (Valores negociados e alvo)
dados_valuation = {
    'Preço Alvo VALE ON': 'R$ 74,37',
    'EV/EBITDA Atual (Negociado)': '3,46x',
    'EBITDA (Estimado)': 'R$ 1.937.000.000,00',
    'Produção Anual de Ferro (toneladas)': '315.000.000,00',
    'Cotação do Minério de Ferro por Tonelada': 'R$ 425,00',
    'Target Price Longo Prazo (Minério)': 'U$ 85,00 @ R$ 5,00',
}

# B. Tabela de Projeções de Fluxo de Caixa (Valores em R$ Milhares - Projeções de 9 Meses)
dados_caixa = {
    'Período': ['2022 (9M)', '2023 (9M)', '2024 (9M)', '2025 (9M)', '2026 (9M)'],
    'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000],
    'Geração de Caixa Operacional (GCO)': [85112400, 50346600, 104153350, 18205850, 17995850],
    'Investimentos em Capital Fixo (Capex)': [-36646000, -41556000, -15412000, -18812000, -16792000],
    'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150]
}
df_caixa = pd.DataFrame(dados_caixa)

# --- 2. FUNÇÕES ---

def gerar_grafico_caixa(dataframe):
    """Gera o gráfico de barras da Geração de Caixa Operacional com formatação profissional."""
    coluna_caixa = 'Geração de Caixa Operacional (GCO)'
    plt.figure(figsize=(12, 6))
    
    # Gráfico de Barras
    ax = sns.barplot(x='Período', y=coluna_caixa, data=dataframe, palette='magma')

    plt.title('3. Geração de Caixa Operacional (GCO) Projetada (R$ Milhões)', fontsize=16, fontweight='bold')
    plt.xlabel('Período (Projeção 9 Meses)', fontsize=12)
    plt.ylabel('GCO', fontsize=12)

    # Formatação para R$ Milhões no Eixo Y e Valores nas Barras
    y_ticks = ax.get_yticks()
    ax.set_yticklabels([f'R$ {y/1000000:.0f}M' for y in y_ticks])

    for p in ax.patches:
        ax.annotate(f'R$ {p.get_height()/1000000:.1f}M', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', xytext=(0, 10), 
                    textcoords='offset points', fontsize=10, fontweight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def imprimir_relatorio_completo():
    """Imprime cabeçalho, KPIs, tabelas e a análise de texto em formato executivo."""
    
    # Cabeçalho e Título
    print("=" * 80)
    print("           Análise de Valuation e Macro: VALE S.A. (Alfa Value)           ")
    print("=" * 80)
    print("Analista: Gustavo Idalino Venceslau Cavalheiro")
    print("Contato: +5511962320573 | Email: gustavovences01@gmail.com")
    
    # 1. Indicadores-Chave
    print("\n## 1. Indicadores-Chave de Valuation")
    print("-" * 40)
    for chave, valor in dados_valuation.items():
        print(f"* **{chave}**: {valor}")
    print("-" * 40)

    # 2. Tabela de Projeção de Fluxo de Caixa
    print("\
