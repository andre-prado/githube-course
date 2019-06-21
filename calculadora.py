# Calculadora que faz soma entre dois numeros
# e também multiplica

entrada = input("Digite + para soma e * para multiplicar: ")

if entrada == "+":
    num1 = int(input("Digite o primeiro número para soma: "))
    num2 = int(input("Digite o segundo número para soma: "))

    soma = num1 + num2

    print("A soma entre {} e {} é de : {}".format(num1, num2, soma))

else:
    num1 = int(input("Digite o primeiro número para multiplicação: "))
    num2 = int(input("Digite o segundo número para multiplicação: "))

    mult = num1 * num2

    print("A multiplicação entre {} e {} é de : {}".format(num1, num2, mult))

    
