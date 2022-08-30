ladoA = int(input("Digite o valor A: "))
ladoB = int(input("Digite o valor B: "))
ladoC = int(input("Digite o valor C: "))

if (ladoA + ladoB > ladoC):
    if(ladoB + ladoC > ladoA):
        if(ladoA + ladoC > ladoB):
            print("Estes valores formam um triangulo")
            if(ladoA > ladoB and ladoA > ladoC ):
                if((ladoA * ladoA) == (ladoB * ladoB) + (ladoC * ladoC)):
                    print("Este triângulo é retângulo")
            elif(ladoB > ladoA and ladoB > ladoC):
                if((ladoB * ladoB) == (ladoA * ladoA) + (ladoC * ladoC)):
                    print("Este triangulo é retângulo")
            elif(ladoC > ladoA and ladoC > ladoB):
                if((ladoC * ladoC) == (ladoA * ladoA) + (ladoB * ladoB)):
                    print("Este triangulo é retângulo")
            else:
                print("E este triângulo não é retângulo")
else:
    print("Esses valores não formam um triangulo!")