# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
# a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
# programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
# previamente definido no código;


Number = int(input('Digite um número: '))


Valor1 = 0
Valor2 = 1


while Valor2 <= Number:

    if Valor2 == Number:
        print("{} pertence à sequência de Fibonacci!".format(Number))
        break
           
    valor = Valor1 + Valor2
    Valor1 = Valor2
    Valor2 = valor

else:
    print ('{} não faz parte da sequência de Fibonacci.'.format(Number))


