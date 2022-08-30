ladoA = int(input("Digite o valor A: "))
ladoB = int(input("Digite o valor B: "))
ladoC = int(input("Digite o valor C: "))

if (ladoA + ladoB > ladoC):
    if(ladoB + ladoC > ladoA):
        if(ladoA + ladoC > ladoB):
            print("Estes valores formam um triangulo")
            if(ladoA != ladoB and ladoC != ladoB and ladoC != ladoA):
                print("E este triângulo é ESCALENO")
            elif(ladoA == ladoB and ladoA != ladoC or ladoC == ladoB and ladoC != ladoA or ladoC == ladoA and ladoC != ladoB):
                print("E este triângulo é ISÓSCELES")
            else:
                print("E este triângulo é EQUILÁTERO")
else:
    print("Esses valores não formam um triangulo!")