# Célula 1: Instalação das dependências!
pip install tabulate
import pandas as pd
import numpy as np

# --- 1. DADOS DE VALUATION DA VALE S.A. (Extraídos do PPTX) ---

# Tabela de Projeções de Fluxo de Caixa (Valores em R$ Milhares)
# Nota: Os valores negativos no Lucro Líquido e Variação NCG foram mantidos conforme o documento.
dados_caixa = {
    'Período': ['01/01/2022 a 30/09/2022', '01/01/2023 a 30/09/2023', '01/01/2024 a 30/09/2024', '01/01/2025 a 30/09/2025', '01/01/2026 a 30/09/2026'],
    'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000],
    'Depreciação e Amortização': [11652000, 11072000, 95004000, 10004000, 10004000],
    'Variação NCG': [4446000, -2199000, -2566000, -1416000, -1516000],
    'Geração de Caixa Operacional': [85112400, 50346600, 104153350, 18205850, 17995850],
    'Investimentos em Capital Fixo': [-36646000, -41556000, -15412000, -18812000, -16792000],
    'Geração de Caixa de Financiamento': [-113499000, -38638000, -85499000, -72499000, -66699000],
    'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150]
}

df_caixa = pd.DataFrame(dados_caixa)

# Outros Dados de Valuation (Extraídos do PPTX)
dados_valuation = {
    [cite_start]'Preço Alvo VALE ON': 'R$ 74,37', # [cite: 33, 46]
    [cite_start]'EV/EBITDA Atual (Negociado)': '3,46x', # [cite: 39]
    [cite_start]'EBITDA (Estimado)': 'R$ 1.937.000.000,00', # [cite: 43]
    [cite_start]'Produção de Ferro (toneladas)': '315.000.000,00', # [cite: 45]
    [cite_start]'Cotação do Ferro por Tonelada': 'R$ 425,00', # [cite: 41]
}

# --- 2. Função de Impressão do Relatório ---

def imprimir_relatorio():
    print("=" * 70)
    print("      RELATÓRIO MACROECONÔMICO E VALUATION: VALE S.A. (Alfa Value)      ")
    print("=" * 70)

    # Destaques do Setor de Mineração (Macro)
    print("\n## 1. Destaques Macroeconômicos do Setor de Mineração")
    print("-" * 50)
    [cite_start]print(f"  * Representatividade no PIB: Próximo de 4% [cite: 3]")
    [cite_start]print(f"  * Faturamento Anual Estimado: R$ 340 bilhões [cite: 3]")
    [cite_start]print(f"  * Crescimento (1º Sem. 2023): 6% [cite: 3]")
    [cite_start]print(f"  * Exportações Nacionais: 30% (U$ 80 bilhões no total) [cite: 3]")
    [cite_start]print(f"  * Risco Macroeconômico: Sinais de recessão Americana/Chinesa e o impacto do 'imposto do pecado' na extração de recursos[cite: 4, 7].")
    [cite_start]print(f"  * ESG/Sustentabilidade: VALE e outras empresas (Gerdau, Votorantim) adotando a Economia Verde e Créditos de Carbono[cite: 5, 9].")

    # Destaques do Valuation da VALE S.A.
    print("\n## 2. Indicadores de Valuation da VALE S.A.")
    print("-" * 50)
    for chave, valor in dados_valuation.items():
        print(f"  * {chave}: {valor}")

    # Tabela de Projeção (Central)
    print("\n### Tabela de Projeção de Fluxo de Caixa (Valores em R$ Milhares)")
    print("  * Nota: Valores apresentados como extraídos. NCG = Necessidade de Capital de Giro.")
    
    # Exibir a Tabela de Projeção usando o Pandas (to_markdown é ideal para visualização limpa)
    # A formatação 'floatfmt' ajuda a exibir números grandes sem notação científica
    print(df_caixa.to_markdown(index=False, floatfmt=",.0f"))

    # Destaques Estratégicos e Financeiros
    print("\n## 3. Estratégia e Observações Finais")
    print("-" * 50)
    [cite_start]print("  * **Estratégia**: Diminuir exposição à China, focando em acordos com Oriente Médio, Ásia e Europa[cite: 127].")
    [cite_start]print("  * **Financeiro**: Maiores despesas relacionadas a Brumadinho[cite: 123]. [cite_start]Há expectativa de melhoras no fluxo de caixa, apesar do Capital de Giro negativo[cite: 123].")
    [cite_start]print("  * **Transição Energética**: O EBITDA se recupera devido a investimentos em infraestrutura e adoção de biocombustíveis e máquinas sustentáveis[cite: 125, 126].")
    [cite_start]print("  * **Minério de Ferro**: O alvo de longo prazo para a cotação é U$ 85,00 (câmbio R$ 5,00)[cite: 124].")
    print("-" * 70)


if __name__ == "__main__":
    imprimir_relatorio()
