num = int(input('Você quer a tabuada de qual número? '))

while(num < 0):
    print("Não pode valores negativos!")
    num = int(input('Digite outro número: '))

intervaloInicial = int(input("Digite o valor inicial do intervalo que deseja a tabuada: "))
intervaloFinal = int(input("Digite o valor final do intervalo que deseja a tabuada: "))

while(intervaloFinal < intervaloInicial):
    print("O valor final do intervalo deve ser maior que o inicial!")
    intervaloFinal = int(print("Digite o valor final do intervalo que deseja a tabuada: "))

i = intervaloFinal

while(i >= intervaloInicial):
    res = num * i
    print(f'{num} * {i} = {res}')
    i = i -1

