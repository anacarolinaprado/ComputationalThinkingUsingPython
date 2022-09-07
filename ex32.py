num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

while(num2 <= num1):
    print("O segundo valor digitado deve ser maior que o primeiro!")
    num2 = int(input("Digite outro número: "))

print(f'Primeiro valor digitado: {num1}')
print(f'Primeiro valor digitado: {num2}')