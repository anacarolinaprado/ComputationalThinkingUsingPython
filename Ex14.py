peso = float(input("Informe o seu peso em kilos: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso / (altura * altura)

if imc < 20:
    print("Abaixo do peso!")
elif imc < 25:
    print("Peso ideal!")
else:
    print("Acima do peso!")