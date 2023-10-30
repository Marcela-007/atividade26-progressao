# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
PA = int(input('Insira o primeiro termo da PA:'))
RAZAO = int(input('Insira a razão da PA:'))
for item in range(10):
 print(item)
 termo = PA + item * RAZAO
 print(F'Termo {item+1}: {termo}')