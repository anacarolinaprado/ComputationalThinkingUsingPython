ladoA = int(input("Digite o valor A: "))
ladoB = int(input("Digite o valor B: "))
ladoC = int(input("Digite o valor C: "))

#Verifica se é ou não um triângulo
if (((ladoA + ladoB) > ladoC) and ((ladoB + ladoC) > ladoA) and ((ladoA + ladoC) > ladoB)):
    print("Estes valores formam um triangulo")
    if(ladoA != ladoB and ladoC != ladoB and ladoC != ladoA):
        print("E este triângulo é ESCALENO")
    elif((ladoA == ladoB and ladoA != ladoC) or (ladoC == ladoB and ladoC != ladoA) or (ladoC == ladoA and ladoC != ladoB)):
        print("E este triângulo é ISÓSCELES")
    else:
        print("E este triângulo é EQUILÁTERO")
else:
    print("Esses valores não formam um triangulo!")