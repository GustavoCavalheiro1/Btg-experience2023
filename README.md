# Análise de Valuation e Macro: VALE S.A.
### Relatório Executivo - Alfa Value
Analista: Gustavo Idalino Venceslau Cavalheiro
Contato: +5511962320573
Email: gustavovences01@gmail.com

[cite_start]**Tese Principal:** A VALE apresenta indicadores de *valuation* que refletem um fluxo de caixa em recuperação[cite: 129]. A diversificação estratégica de mercado e o foco em ESG mitigam riscos macroeconômicos e de dependência da China.
# Célula de Código 1: Setup, Dados e Funções

# Instalação das dependências (remova o '#' para executar no seu Colab)
# !pip install tabulate
# !pip install matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. DADOS DE VALUATION DA VALE S.A. (Extraídos do PPTX e PDF) ---

# A. Indicadores-Chave
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
    'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000],
    'Geração de Caixa Operacional (GCO)': [85112400, 50346600, 104153350, 18205850, 17995850],
    'Investimentos em Capital Fixo (Capex)': [-36646000, -41556000, -15412000, -18812000, -16792000],
    'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150]
}
df_caixa = pd.DataFrame(dados_caixa)

# --- 2. Função para Gerar o Gráfico ---

def gerar_grafico_caixa(dataframe):
    """Gera o gráfico de barras da Geração de Caixa Operacional com formatação profissional."""
    coluna_caixa = 'Geração de Caixa Operacional (GCO)'
    
    plt.figure(figsize=(12, 6))
    
    ax = sns.barplot(
        x='Período', 
        y=coluna_caixa, 
        data=dataframe, 
        palette='magma'
    )
    
    plt.title('3. Geração de Caixa Operacional (GCO) Projetada (R$ Milhões)', fontsize=16, fontweight='bold')
    plt.xlabel('Período (Projeção 9 Meses)', fontsize=12)
    plt.ylabel('GCO', fontsize=12)

    # Conversão e Formatação para R$ Milhões no Eixo Y
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
    
    # Célula de Código 2: Execução do Relatório

imprimir_indicadores_e_tabela()
gerar_grafico_caixa(df_caixa)

# Célula 3: Exibição de KPIs e Tabela de Projeções

print("## Indicadores-Chave de Valuation")
print("-" * 40)
for chave, valor in dados_valuation.items():
    print(f"* **{chave}**: {valor}")
print("-" * 40)

print("\n## Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
# Mostra apenas as colunas essenciais para uma análise rápida de caixa
df_exibicao = df_caixa[['Período', 'Geração de Caixa Operacional (GCO)', 'Investimentos em Capital Fixo (Capex)', 'Posição do Caixa Final']]
print(df_exibicao.to_markdown(index=False, floatfmt=",.0f"))
****
## 4. Análise e Conclusões

### Destaques Macroeconômicos
* [cite_start]O setor de mineração representa **~4% do PIB** [cite: 118] [cite_start]e **~30% das exportações nacionais** (U$80B)[cite: 118].
* [cite_start]**Riscos & Oportunidades:** Há riscos de recessão nos EUA e na China [cite: 122][cite_start], além do impacto do "imposto do pecado" na extração[cite: 119]. [cite_start]A VALE se beneficia de sua alta exposição cambial com a valorização do Dólar em suas receitas[cite: 108].
* [cite_start]**Sustentabilidade:** A VALE está investindo fortemente em tecnologias para neutralizar emissões de carbono e adota biocombustíveis e máquinas sustentáveis[cite: 120, 110].

### Análise Fundamentalista (VALE S.A.)
* [cite_start]**Caixa e Liquidez:** A Geração de Caixa Operacional (GCO) mostra recuperação, e há expectativas de melhoria no fluxo de caixa apesar do Capital de Giro negativo[cite: 107].
* [cite_start]**Estratégia e Crescimento:** A empresa busca **diminuir exposição à China** [cite: 111][cite_start], focando em acordos com o Oriente Médio, Ásia e Europa[cite: 111, 112].
* [cite_start]**Minério de Ferro:** O preço do minério de ferro mostra-se resiliente [cite: 127][cite_start], com alvo de longo prazo em **U$ 85,00**[cite: 108].

### Recomendação
[cite_start]O preço alvo de **R$ 74,37** [cite: 17, 31] é suportado pela resiliência do minério de ferro e pela estratégia de diversificação de clientes. A recuperação do fluxo de caixa e o foco em mercados desenvolvidos justificam uma visão **positiva** de longo prazo.
