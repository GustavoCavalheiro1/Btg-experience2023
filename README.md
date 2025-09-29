# # Análise de Valuation e Macro: VALE S.A.
# ### Relatório Executivo - Alfa Value
# Analista: Gustavo Idalino Venceslau Cavalheiro  <--- LINHA QUE DEU ERRO AGORA ESTÁ COMENTADA
# Contato: +5511962320573
# Email: gustavovences01@gmail.com

# **Tese Principal:** A VALE apresenta indicadores de *valuation* que refletem um fluxo de caixa em recuperação. A diversificação...
# Agora, o código Python válido deve seguir abaixo:


!pip install tabulate
import pandas as pd
# ... (restante do seu código)
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
    print("\n## 2. Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
    print("Nota: Projeções de 9 meses (9M)")
    
    # Seleciona colunas essenciais para análise de caixa
    df_exibicao = df_caixa[['Período', 'Geração de Caixa Operacional (GCO)', 'Investimentos em Capital Fixo (Capex)', 'Posição do Caixa Final']]
    print(df_exibicao.to_markdown(index=False, floatfmt=",.0f"))
    
    # 4. Análise e Conclusões
    print("\n" + "=" * 80)
    print("                        4. Análise e Conclusões                        ")
    print("=" * 80)

    print("\n### 4.1. Destaques Macroeconômicos")
    print("* O setor de mineração representa próximo de 4% do PIB, com faturamento de ~R$340 bilhões, e 30% das exportações nacionais (U$80B).")
    print("* Risco: Sinais de recessão Americana e Chinesa, e o impacto do 'imposto do pecado' na extração.")
    print("* Oportunidade: A VALE se beneficia de sua alta exposição cambial e da valorização do Dólar em suas receitas.")

    print("\n### 4.2. Análise Fundamentalista")
    print("* **Caixa e Liquidez**: A Geração de Caixa Operacional (GCO) tem salto projetado de R$ 50B (2023) para **R$ 104B (2024)**. O Capital de Giro negativo mantém expectativas de melhoras no fluxo de caixa.")
    print("* **Despesas**: As maiores despesas ainda estão relacionadas aos processos de Brumadinho.")
    print("* **Estratégia**: Movimento estratégico para diminuir exposição à China, focando em acordos com o Oriente Médio, Ásia e Europa.")

    print("\n### 4.3. Fatores ESG e Recomendação")
    print("* **Fatores ESG**: A VALE investe fortemente em tecnologias para neutralizar emissões de carbono e adota biocombustíveis e máquinas sustentáveis.")
    print("* **Recomendação**: O preço alvo de **R$ 74,37** é suportado pela resiliência do minério de ferro e pela estratégia de diversificação. Visão **POSITIVA** de longo prazo.")
    print("=" * 80)


# --- 3. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    imprimir_relatorio_completo()
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

# Célula 4: Geração do Gráfico de Análise de Caixa

def gerar_grafico_caixa(dataframe):
    """Gera o gráfico de barras da Geração de Caixa Operacional."""
    coluna_caixa = 'Geração de Caixa Operacional (GCO)'

    plt.figure(figsize=(12, 6))

    ax = sns.barplot(
        x='Período',
        y=coluna_caixa,
        data=dataframe,
        palette='magma', # Paleta profissional
        hue='Período', # Address FutureWarning: Passing `palette` without assigning `hue`
        legend=False # Set legend to False as suggested by the warning
    )

    plt.title('Geração de Caixa Operacional (GCO) Projetada (R$ Milhões)', fontsize=16, fontweight='bold')
    plt.xlabel('Período (9 Meses)', fontsize=12)
    plt.ylabel('GCO', fontsize=12)

    # Conversão e Formatação para R$ Milhões no Eixo Y
    # Address UserWarning: set_ticklabels() should only be used with a fixed number of ticks
    y_ticks = ax.get_yticks()
    ax.yaxis.set_major_locator(plt.FixedLocator(y_ticks)) # Set a fixed locator
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
