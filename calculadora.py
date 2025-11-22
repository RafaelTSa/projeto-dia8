# Define nossa função
def calculate():
    operação = input('''
Por favor, selecione a operação desejada:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')
    numero_1 = int(input("Digite seu primeiro número: "))
    numero_2 = int(input("Digite seu segundo número: "))

    # Soma
    if operação == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    # Subtração
    elif operação == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    # Multiplicação
    elif operação == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    # Divisão
    elif operação == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

# Chamamos calculate() fora da função
calculate()

