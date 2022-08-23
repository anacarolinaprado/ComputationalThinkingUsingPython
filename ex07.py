p1 = float(input('Digite o valor do primeiro produto: '))
p2 = float(input('Digite o valor do segundo produto: '))
p3 = float(input('Digite o valor do terceiro produto: '))
p4 = float(input('Digite o valor do quarto produto: '))
p5 = float(input('Digite o valor do quinto produto: '))

total = p1 + p2 + p3 + p4 + p5

print('O total da compra foi R$ ', total)

pagamento = float(input('Pagamento: '))

troco = pagamento - total

print('Troco no valor de R$', troco)