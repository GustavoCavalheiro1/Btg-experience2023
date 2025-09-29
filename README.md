# Análise de Valuation e Macro: VALE S.A.
### Relatório Executivo - Alfa Value
Analista: Gustavo Idalino Venceslau Cavalheiro
Contato: +5511962320573
Email: gustavovences01@gmail.com

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# --- 1. DADOS DE VALUATION (VALE S.A.) ---

# A. Indicadores-Chave (Valores negociados e alvo)
dados_valuation = {
    [cite_start]'Preço Alvo VALE ON': 'R$ 74,37', # [cite: 33, 47]
    [cite_start]'EV/EBITDA Atual (Negociado)': '3,46x', # [cite: 39]
    [cite_start]'EBITDA (Estimado)': 'R$ 1.937.000.000,00', # [cite: 29, 43]
    [cite_start]'Produção Anual de Ferro (toneladas)': '315.000.000,00', # [cite: 31, 45]
    [cite_start]'Cotação do Minério de Ferro por Tonelada': 'R$ 425,00', # [cite: 27, 41]
    [cite_start]'Target Price Longo Prazo (Minério)': 'U$ 85,00 @ R$ 5,00', # [cite: 124]
}

# B. Tabela de Projeções de Fluxo de Caixa (Valores em R$ Milhares - Projeções de 9 Meses)
dados_caixa = {
    'Período': ['2022 (9M)', '2023 (9M)', '2024 (9M)', '2025 (9M)', '2026 (9M)'],
    'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000],
    [cite_start]'Geração de Caixa Operacional (GCO)': [85112400, 50346600, 104153350, 18205850, 17995850], # [cite: 76, 77, 78, 79, 80]
    'Investimentos em Capital Fixo (Capex)': [-36646000, -41556000, -15412000, -18812000, -16792000],
    [cite_start]'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150] # [cite: 118, 119, 120, 121, 122]
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

    # Formatação para R$ Milhões no Eixo Y
    y_ticks = ax.get_yticks()
    ax.set_yticklabels([f'R$ {y/1000000:.0f}M' for y in y_ticks])
    
    # Adicionar os valores exatos (em R$ Milhões) nas barras
    for p in ax.patches:
        ax.annotate(f'R$ {p.get_height()/1000000:.1f}M', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 10), 
                    textcoords='offset points',
                    fontsize=10,
                    fontweight='bold')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def imprimir_indicadores_e_tabela():
    """Imprime os KPIs, a Tabela de Projeção e a Análise em formato Executivo."""
    print("=" * 80)
    print("                    Relatório Executivo: VALE S.A. (Alfa Value)                    ")
    print("=" * 80)
    print("Analista: Gustavo Idalino Venceslau Cavalheiro")
    print("\n## 1. Indicadores-Chave de Valuation")
    print("-" * 40)
    for chave, valor in dados_valuation.items():
        print(f"* **{chave}**: {valor}")
    print("-" * 40)

    print("\n## 2. Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
    print("Nota: Projeções de 9 meses (9M)")
    
    # Seleciona colunas essenciais para análise de caixa
    df_exibicao = df_caixa[['Período', 'Geração de Caixa Operacional (GCO)', 'Investimentos em Capital Fixo (Capex)', 'Posição do Caixa Final']]
    print(df_exibicao.to_markdown(index=False, floatfmt=",.0f"))

    # --- Análise em Texto ---
    print("\n" + "=" * 80)
    print("                        4. Análise e Conclusões                        ")
    print("=" * 80)

    print("\n### Destaques Macroeconômicos")
    [cite_start]print("* O setor de mineração representa ~4% do PIB, com faturamento de ~R$340 bilhões, e ~30% das exportações nacionais (U$80B). [cite: 3]")
    [cite_start]print("* Risco: Sinais de recessão Americana e Chinesa, e impacto do 'imposto do pecado' na extração. [cite: 7, 4]")
    [cite_start]print("* Oportunidade: A VALE se beneficia de sua alta exposição cambial e da valorização do Dólar em suas receitas. [cite: 124]")
    [cite_start]print("* Crescimento: O setor cresceu 6% no primeiro semestre de 2023. [cite: 3]")

    print("\n### Análise Fundamentalista (VALE S.A.)")
    [cite_start]print("* Caixa e Liquidez: A Geração de Caixa Operacional (GCO) tem salto projetado de R$ 50B (2023) para R$ 104B (2024). Mantém Capital de Giro negativo, mas há expectativas de melhoria no fluxo de caixa. [cite: 123]")
    [cite_start]print("* Despesas: As maiores despesas ainda estão relacionadas aos processos de Brumadinho. [cite: 123]")
    [cite_start]print("* Estratégia e Crescimento: Movimento estratégico para diminuir exposição à China, focando em acordos com o Oriente Médio, Ásia e Europa. [cite: 127, 128]")

    print("\n### Fatores ESG e Transição Energética")
    [cite_start]print("* A VALE está investindo em tecnologias para neutralizar emissões de carbono e adota biocombustíveis e máquinas sustentáveis. [cite: 5, 126]")
    [cite_start]print("* Esta transição contribui para a recuperação do EBITDA. [cite: 125]")
    print("=" * 80)


# --- 3. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    imprimir_indicadores_e_tabela()
    gerar_grafico_caixa(df_caixa)
    
## Análise e Conclusões

### 1. Destaques Macroeconômicos
* O setor de mineração representa ~4% do PIB e ~30% das exportações nacionais (U$80B)[cite: 118].
* **Riscos & Oportunidades:** Há riscos de recessão nos EUA e na China [cite: 122], além do impacto do "imposto do pecado" na extração[cite: 119]. Contudo, a VALE se beneficia de sua alta exposição cambial com a valorização do Dólar em suas receitas[cite: 108].

### 2. Análise Fundamentalista (VALE S.A.)
* **Caixa e Liquidez:** A Geração de Caixa Operacional (GCO) mostra uma recuperação notável, saltando de R$ 50B em 2023 para R$ 104B em 2024 (projeção 9M). O GCO se mostra resiliente apesar do Capital de Giro negativo[cite: 107].
* **Despesas:** As maiores despesas ainda estão relacionadas aos processos de Brumadinho[cite: 107].
* **Estratégia e Crescimento:** A empresa está em um movimento estratégico de diminuição da exposição à China, fechando acordos com o Oriente Médio, Ásia e Europa[cite: 111]. Este movimento visa acordos ambientais e aumento de receita[cite: 112].

### 3. Fatores ESG e Transição Energética
* A VALE está investindo em tecnologias para neutralizar emissões de carbono [cite: 120] e adota biocombustíveis e máquinas sustentáveis[cite: 110]. Esta transição contribui para a recuperação do EBITDA [cite: 109], alinhando a empresa com a **Economia Verde**[cite: 124].

## Recomendação
O preço alvo de **R$ 74,37** é suportado pela resiliência do minério de ferro e pela estratégia de diversificação de clientes. A recuperação do fluxo de caixa e o foco em mercados desenvolvidos justificam uma visão **positiva** de longo prazo.
