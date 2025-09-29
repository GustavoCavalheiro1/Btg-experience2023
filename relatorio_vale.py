import pandas as pd
import numpy as np

# --- 1. DADOS DE VALUATION DA VALE S.A. (Extraídos do PPTX) ---

# Tabela de Projeções de Fluxo de Caixa (Valores em R$ Milhares - Adicionado '000' para clareza)
# Os valores negativos (-XXXX) no Lucro Líquido e Variação NCG foram mantidos conforme o documento.
dados_caixa = {
    'Período': ['01/01/2022 a 30/09/2022', '01/01/2023 a 30/09/2023', '01/01/2024 a 30/09/2024', '01/01/2025 a 30/09/2025', '01/01/2026 a 30/09/2026'],
    [cite_start]'Lucro Líquido': [86424000, -2199000, -2566000, -1416000, -1516000], # [cite: 58, 59, 60, 61, 62]
    [cite_start]'Depreciação e Amortização': [11652000, 11072000, 95004000, 10004000, 10004000], # [cite: 64, 65, 66, 67, 68]
    [cite_start]'Variação NCG': [4446000, -2199000, -2566000, -1416000, -1516000], # [cite: 70, 71, 72, 73, 74]
    [cite_start]'Geração de Caixa Operacional': [85112400, 50346600, 104153350, 18205850, 17995850], # [cite: 76, 77, 78, 79, 80]
    [cite_start]'Investimentos em Capital Fixo': [-36646000, -41556000, -15412000, -18812000, -16792000], # [cite: 82, 83, 84, 85, 86]
    [cite_start]'Geração de Caixa de Financiamento': [-113499000, -38638000, -85499000, -72499000, -66699000], # [cite: 100, 101, 102, 103, 104]
    [cite_start]'Posição do Caixa Final': [-5637600, -2916400, 148183350, -11256150, -646150] # [cite: 118, 119, 120, 121, 122]
}

df_caixa = pd.DataFrame(dados_caixa)

# Outros Dados de Valuation (Extraídos do PPTX)
dados_valuation = {
    [cite_start]'Preço Alvo VALE ON': 'R$ 74,37', # [cite: 32, 46]
    [cite_start]'EV/EBITDA Atual (Negociado)': '3,46x', # [cite: 39] [cite_start](O documento também menciona 1,67x e 3,46x, mas 3,46x é a negociação atual [cite: 14])
    [cite_start]'EBITDA (Estimado)': 'R$ 1.937.000.000,00', # [cite: 29, 43]
    [cite_start]'Produção de Ferro (toneladas)': '315.000.000,00', # [cite: 31, 45]
    [cite_start]'Cotação do Ferro por Tonelada': 'R$ 425,00', # [cite: 27, 41]
}

# --- 2. DESTAQUES MACROECONÔMICOS (Extraídos do PDF) ---

def imprimir_destaques():
    print("=" * 60)
    print("  RELATÓRIO MACROECONÔMICO E VALUATION: VALE S.A.  ")
    print("  Autor: Gustavo Idalino Venceslau Cavalheiro")
    print("=" * 60)

    # Destaques do Setor de Mineração (Macro)
    print("\n## 1. Destaques Macroeconômicos do Setor de Mineração")
    print("-" * 50)
    [cite_start]print(f"  * Representatividade no PIB: Próximo de 4% [cite: 3]")
    [cite_start]print(f"  * Faturamento Anual Estimado: R$ 340 bilhões [cite: 3]")
    [cite_start]print(f"  * Crescimento (1º Sem. 2023): 6% [cite: 3]")
    [cite_start]print(f"  * Exportações Nacionais: 30% (U$ 80 bilhões no total) [cite: 3]")
    [cite_start]print(f"  * Empregos: 2 milhões (diretos e indiretos) [cite: 3]")
    [cite_start]print(f"  * Risco Macroeconômico: Recessão Americana/Chinesa e 'imposto do pecado' (tributação sobre extração) [cite: 7, 4]")
    [cite_start]print(f"  * ESG/Sustentabilidade: Empresas como VALE, Gerdau e Votorantim estão adotando a Economia Verde e Créditos de Carbono. [cite: 5, 9]")

    # Destaques do Valuation da VALE S.A.
    print("\n## 2. Destaques de Valuation da VALE S.A.")
    print("-" * 50)
    for chave, valor in dados_valuation.items():
        print(f"  * {chave}: {valor}")

    print("\n### Tabela de Projeção de Fluxo de Caixa (em R$)")
    print("  * Nota: Valores apresentados como extraídos, incluindo NCG e Lucro Líquido negativos nas projeções. Valores em milhares.")
    
    # Exibir a Tabela de Projeção
    # Para melhor leitura no terminal, vamos usar 'to_markdown' ou 'to_string'
    print(df_caixa.to_markdown(index=False, floatfmt=",.0f"))

    # Destaques Estratégicos e Financeiros
    print("\n## 3. Estratégia e Observações da VALE")
    print("-" * 50)
    [cite_start]print("  * **Estratégia**: Diminuir exposição à China, buscando acordos com Oriente Médio, Ásia e Europa para aumentar receitas e entrar em acordos ambientais. [cite: 127, 128]")
    [cite_start]print("  * **Financeiro**: Maiores despesas ligadas aos processos de Brumadinho. Há expectativas de melhoras no fluxo de caixa, apesar do Capital de Giro negativo. [cite: 123]")
    [cite_start]print("  * **Transição Energética**: Recuperação do EBITDA devido a investimentos em novas máquinas, infraestrutura e adoção de biocombustíveis e máquinas sustentáveis. [cite: 125, 126]")
    [cite_start]print("  * **Minério de Ferro**: Preços resilientes em 2023. O alvo de longo prazo é U$ 85,00 no câmbio de R$ 5,00. [cite: 12, 124]")


if __name__ == "__main__":
    imprimir_destaques()
