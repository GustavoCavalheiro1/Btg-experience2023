import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# --- 1. DADOS DE VALUATION (VALE S.A.) ---

# A. Indicadores-Chave (Valores negociados e alvo)
dados_valuation = {
    [cite_start]'Preço Alvo VALE ON': 'R$ 74,37', # [cite: 17, 31]
    [cite_start]'EV/EBITDA Atual (Negociado)': '3,46x', # [cite: 23, 129]
    [cite_start]'EBITDA (Estimado)': 'R$ 1.937.000.000,00', # [cite: 13, 27]
    [cite_start]'Produção Anual de Ferro (toneladas)': '315.000.000,00', # [cite: 15, 29]
    [cite_start]'Cotação do Minério de Ferro por Tonelada': 'R$ 425,00', # [cite: 11, 25]
    [cite_start]'Target Price Longo Prazo (Minério)': 'U$ 85,00 @ R$ 5,00', # [cite: 108]
}

# B. Tabela de Projeções de Fluxo de Caixa (Valores em R$ Milhares - Projeções de 9 Meses)
dados_caixa = {
    'Período': ['2022 (9M)', '2023 (9M)', '2024 (9M)', '2025 (9M)', '2026 (9M)'],
    [cite_start]'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000], # [cite: 42, 43, 44, 45, 46]
    [cite_start]'Geração de Caixa Operacional (GCO)': [85112400, 50346600, 104153350, 18205850, 17995850], # [cite: 60, 61, 62, 63, 64]
    [cite_start]'Investimentos em Capital Fixo (Capex)': [-36646000, -41556000, -15412000, -18812000, -16792000], # [cite: 66, 67, 68, 69, 70]
    [cite_start]'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150] # [cite: 102, 103, 104, 105, 106]
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
    print("\n## 2. Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
    print("Nota: Projeções de 9 meses (9M)")
    
    df_exibicao = df_caixa[['Período', 'Geração de Caixa Operacional (GCO)', 'Investimentos em Capital Fixo (Capex)', 'Posição do Caixa Final']]
    print(df_exibicao.to_markdown(index=False, floatfmt=",.0f"))
    
    # 4. Análise e Conclusões
    print("\n" + "=" * 80)
    print("                        4. Análise e Conclusões                        ")
    print("=" * 80)

    print("\n### 4.1. Destaques Macroeconômicos")
    [cite_start]print("* O setor de mineração representa próximo de 4% do PIB, com faturamento de ~R$340 bilhões, e 30% das exportações nacionais (U$80B)[cite: 118].")
    [cite_start]print("* Risco: Sinais de recessão Americana e Chinesa, e o impacto do 'imposto do pecado' na extração[cite: 122, 119].")
    [cite_start]print("* Oportunidade: A VALE se beneficia de sua alta exposição cambial e da valorização do Dólar em suas receitas[cite: 108].")

    print("\n### 4.2. Análise Fundamentalista")
    [cite_start]print("* **Caixa e Liquidez**: A Geração de Caixa Operacional (GCO) tem salto projetado de R$ 50B (2023) para **R$ 104B (2024)**. O Capital de Giro negativo mantém expectativas de melhoras no fluxo de caixa[cite: 129, 107].")
    [cite_start]print("* **Despesas**: As maiores despesas ainda estão relacionadas aos processos de Brumadinho[cite: 107].")
    [cite_start]print("* **Estratégia**: Movimento estratégico para diminuir exposição à China, focando em acordos com o Oriente Médio, Ásia e Europa[cite: 111, 112].")

    print("\n### 4.3. Fatores ESG e Recomendação")
    [cite_start]print("* **Fatores ESG**: A VALE investe fortemente em tecnologias para neutralizar emissões de carbono e adota biocombustíveis e máquinas sustentáveis[cite: 120, 110].")
    [cite_start]print("* **Recomendação**: O preço alvo de **R$ 74,37** é suportado pela resiliência do minério de ferro e pela estratégia de diversificação. Visão **POSITIVA** de longo prazo[cite: 17, 31, 127].")
    print("=" * 80)


# --- 3. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    imprimir_relatorio_completo()
    gerar_grafico_caixa(df_caixa)
