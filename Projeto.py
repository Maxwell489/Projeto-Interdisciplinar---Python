#Primeira parte
import math

print("Está é uma calculadora onde você pode entrar com o numero que deseja e fazer o calculo")
print("Digite abaixo qual operação você deseja fazer.")
print("Se for somar digite +.")
print("Se for subtrair digite -.")
print("Se for multiplicar digite *.")
print("Se for dividir digite /.")

op = input("Digite sua operação: ")

print("Digite a baixo os dois numeros que deseja fazer a operação.")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

f1 = n1+n2
f2 = n1-n2
f3 = n1*n2
f4 = n1/n2

if op == "+":
    print("O valor sera: ", f1 )

if op =="-":
    print("O valor sera: ", f2 )

if op =="*":
    print("O valor sera: ", f3 )

if op =="/":
    print("O valor sera: ", f4 )

#Segunda Parte

print('''Agora você vai escolher umas das opções para fazer a coversão:
[1] Para Binario.
[2] Para Octal.
[3] Para Hexemadecimal.''')
opc = int(input("Digite sua opção: "))
num = int(input("Agora digite seu número decimal: "))

if opc == 1:
    print("{}Seu número convertido para BINARIO vai ficar igual: {}".format(num, bin(num)[2:]))

elif opc == 2:
     print("{}Seu número convertido OCTAL vai ficar igual: {}".format(num, oct(num)[2:]))

elif opc == 3:
     print("{}Seu número convertido HEXEMADECIMAL vai ficar igual:{} ".format(num, hex(num)[2:]))

else:
    print("Opção invalida")