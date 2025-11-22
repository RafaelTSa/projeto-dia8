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
print('{} + {} = '.format(numero_1, numero_2))
print(numero_1 + numero_2)

# Subtração
print('{} - {} = '.format(numero_1, numero_2))
print(numero_1 - numero_2)

# Multiplicação
print('{} * {} = '.format(numero_1, numero_2))
print(numero_1 * numero_2)

# Divisão
print('{} / {} = '.format(numero_1, numero_2))
print(numero_1 / numero_2)

