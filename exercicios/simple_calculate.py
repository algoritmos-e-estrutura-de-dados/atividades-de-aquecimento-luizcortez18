print(" Informe respectivamente o código do produto, quantidade e valor ")
linha1 = input().split(" ")
print(" Informe respectivamente o código do produto, quantidade e valor ")
linha2 = input().split(" ")
codigo1, quantidade1, valor1 = linha1
codigo2, quantidade2, valor2 = linha2
total = (int(quantidade1) * float(valor1)) + (int(quantidade2) * float(valor2))
print(f'VALOR A PAGAR: R$ {total:.2f}')      