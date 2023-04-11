##3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
# faça um programa, na linguagem que desejar, que calcule e retorne:
##• O menor valor de faturamento ocorrido em um dia do mês;
##• O maior valor de faturamento ocorrido em um dia do mês;
##• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

##IMPORTANTE:
##a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
##b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;

import json

with open("exercicio 3//dados.json") as meu_json:
    dados = json.load(meu_json)


valores = []
valorSemZero = []
contador = 0

for dado in dados:
    valores.append(dado['valor'])
    if dado['valor'] != 0:
        valorSemZero.append(dado['valor'])
    if dado['valor'] > sum(valorSemZero) / len(valorSemZero):
        contador += 1


print('Maior faturamento: ' + str( max(valores)))
print('Menor faturamento: ' + str(min(valorSemZero)) + " sem contar os dias zerados." )
print('Média: ' + str(sum(valorSemZero) / len(valorSemZero)))
print(str(contador) + ' dias o faturamento foi maior do que a média mensal' )
