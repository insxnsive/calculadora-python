from codecs import oem_decode
from string import octdigits


while True:
    print(" ")
    print("=-=-=-=-=-=-=-=-=")
    number1 = int(input("Escolha o primeiro número: "));
    print("----------------")
    print("Adição: +")
    print("Subtração: -")
    print("Multiplicação: x")
    print("Divisão: /")
    print(" ")
    operação = input("Agora a operação: "); 
    
    print("----------------")
    number2 = int(input('Escolha o segundo número: '));
    print("----------------")

    if operação == 'x':
        resultado = number1 * number2

    elif operação == '/':
        resultado = number1 / number2

    elif operação == '+':
        resultado = number1 + number2

    elif operação == '-':
        resultado = number1 - number2
    else: resultado = "Operação efetuada errado."

    print(str(number1) + ' ' + str(operação) + ' ' + str(number2) + " = " + str(resultado)) 
    print("=-=-=-=-=-=-=-=-=")