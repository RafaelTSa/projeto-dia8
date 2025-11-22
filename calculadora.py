# Define nossa função
def calculate():
    operacao = input('''
Por favor, selecione a operação desejada:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')
    try:
        numero_1 = int(input("Digite seu primeiro número: "))
        numero_2 = int(input("Digite seu segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        again()
        return

    # Soma
    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    # Subtração
    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    # Multiplicação
    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    # Divisão
    elif operacao == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

    # Após o cálculo, pergunte se o usuário quer continuar
    again()

# Define função again() para perguntar se o usuario quer usar a calculadora de novo
def again():
    # Recebe input do usuario
    calc_again = input('''
Você quer calcular de novo?
Por favor digite S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais!')
    else:
        again()

# chama calculate() fora da função
calculate()
