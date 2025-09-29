# Análise de Valuation e Macro: VALE S.A.
### Relatório Executivo - Alfa Value
Analista: Gustavo Idalino Venceslau Cavalheiro
Contato: +5511962320573
Email: gustavovences01@gmail.com

# Célula de Código 1: Setup, Dados e Funções

# Instalação das dependências (descomente e execute se necessário)
# !pip install tabulate
# !pip install matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. DADOS DE VALUATION (VALE S.A.) ---

# A. Indicadores-Chave (Valores negociados e alvo)
dados_valuation = {
    [cite_start]'Preço Alvo VALE ON': 'R$ 74,37'[cite: 17, 31],
    [cite_start]'EV/EBITDA Atual (Negociado)': '3,46x'[cite: 23, 129],
    [cite_start]'EBITDA (Estimado)': 'R$ 1.937.000.000,00'[cite: 13, 27],
    [cite_start]'Produção Anual de Ferro (toneladas)': '315.000.000,00'[cite: 15, 29],
    [cite_start]'Cotação do Minério de Ferro por Tonelada': 'R$ 425,00'[cite: 11, 25],
    [cite_start]'Target Price Longo Prazo (Minério)': 'U$ 85,00 @ R$ 5,00'[cite: 108],
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
    """Gera o gráfico de barras da Geração de Caixa Operacional."""
    coluna_caixa = 'Geração de Caixa Operacional (GCO)'
    plt.figure(figsize=(12, 6))
    
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
    """Imprime os KPIs e a Tabela de Projeção."""
    print("## 1. Indicadores-Chave de Valuation")
    print("-" * 40)
    for chave, valor in dados_valuation.items():
        print(f"* **{chave}**: {valor}")
    print("-" * 40)

    print("\n## 2. Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
    print("Nota: Projeções de 9 meses (9M)")
    
    # Seleciona colunas essenciais para análise de caixa
    df_exibicao = df_caixa[['Período', 'Geração de Caixa Operacional (GCO)', 'Investimentos em Capital Fixo (Capex)', 'Posição do Caixa Final']]
    print(df_exibicao.to_markdown(index=False, floatfmt=",.0f"))
    # Célula de Código 2: Execução do Relatório

imprimir_indicadores_e_tabela()
gerar_grafico_caixa(df_caixa)

## 4. Análise e Conclusões

### Destaques Macroeconômicos
* [cite_start]O setor de mineração representa **~4% do PIB** [cite: 118] [cite_start]e **~30% das exportações nacionais** (U$80B)[cite: 118].
* [cite_start]Houve um **crescimento de 6%** no setor no primeiro semestre de 2023[cite: 118].
* [cite_start]**Riscos & Oportunidades:** Há sinais de recessão Americana e Chinesa [cite: 122][cite_start], e o "imposto do pecado" pode impactar o PIB através do aumento de preços[cite: 119]. [cite_start]A entrada de dólares no Brasil por meio da VALE a beneficia nas receitas[cite: 108].
* [cite_start]**Sustentabilidade:** A VALE está investindo em tecnologias para neutralizar as emissões de carbono e adota biocombustíveis e máquinas sustentáveis[cite: 120, 110].

### Análise Fundamentalista (VALE S.A.)
* [cite_start]**Caixa e Liquidez:** As maiores despesas são relacionadas aos processos de Brumadinho[cite: 107]. [cite_start]A empresa mantém o Capital de Giro negativo, mas há expectativas de melhoras no fluxo de caixa[cite: 107].
* [cite_start]**Estratégia e Crescimento:** A empresa busca **diminuir exposição à China**, focando em acordos com o Oriente Médio, Ásia e Europa[cite: 111]. [cite_start]O objetivo é aumentar a receita e entrar em acordos ambientais com países desenvolvidos[cite: 112, 113].
* [cite_start]**Minério de Ferro:** O preço do minério de ferro está resiliente ao longo de 2023 [cite: 127][cite_start], com alvo de longo prazo em **U$ 85,00**[cite: 108].

### Recomendação
O preço alvo de **R$ 74,37** é suportado pela resiliência do minério de ferro e pela estratégia de diversificação de clientes. A recuperação do fluxo de caixa e o foco em mercados desenvolvidos justificam uma visão **positiva** de longo prazo.
