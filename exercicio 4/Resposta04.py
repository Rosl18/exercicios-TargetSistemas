# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada 
# estado teve dentro do valor total mensal da distribuidora.



dicio_faturamento = {
    "SP": 67836.43,"RJ": 36678.66,"MG": 29229.88,"ES": 27165.48,"Outros": 19849.53
}

Valores_dicio = sum(dicio_faturamento.values())

estados = 0
valor = 0

percentual = {estados: (valor / Valores_dicio) * 100 for estados, valor in dicio_faturamento.items()}

for estados, percentuais in percentual.items():
   print(f"{estados } - {percentuais:.2f}%")
