peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros: "))
sexo  = input("Informe o seu gênero (F/M): ")

imc = peso / (altura * altura)

if( sexo == 'M'):
    if(imc < 20):
        print("Abaixo do peso!")
    elif(imc < 25):
        print("Peso ideal")
    else:
        print("Acima do peso")
else:
    if(imc < 19):
        print("Abaixo do peso")
    elif(imc < 24):
        print("Peso ideal")
    else:
        print("Acima do peso")
