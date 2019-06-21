# Calculadora que faz soma, multiplicação e subtração 

entrada = input("Digite (+) para soma, (*) para multiplicar ou (-) para subtrair: ")

if entrada == "+":
    num1 = int(input("Digite o primeiro número para soma: "))
    num2 = int(input("Digite o segundo número para soma: "))

    soma = num1 + num2

    print("A soma entre {} e {} é de : {}".format(num1, num2, soma))

elif entrada =="*":
    num1 = int(input("Digite o primeiro número para multiplicação: "))
    num2 = int(input("Digite o segundo número para multiplicação: "))

    mult = num1 * num2

    print("A multiplicação entre {} e {} é de : {}".format(num1, num2, mult))
else:
    num1 = int(nput("Digite o primeiro número para subtrair: "))
    num2 = int(input("Digite o segundo número para subtrair: "))

    sub = num1 - num2

    print("{} subtraído de {} é : {}".format(num1,num2,num3))
    
