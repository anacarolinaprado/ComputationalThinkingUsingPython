num = int(input("Digite um número: "))

while (num < 0):
    print("Entre somente com valores positivos!")
    num = int(input("Digite outro número: "))


print(f'Número digitado: {num}')