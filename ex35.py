num = int(input('Digite um número: '))

while(num <= 0):
    print("Não pode valores negativos!")
    num = int(input('Digite outro número: '))

i = 1

while(i <= 10):
    t = num * i
    print(f'{num} * {i} = {t}')
    i = i + 1