print("Informe os valores para comparação: ")
valor = input().split(" ")
a,b,c = valor

maiorab = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
maiorabc = (int(maiorab) + int(c) + abs(int(maiorab) - int(c)))/2

print(f"{maiorabc} eh o maior ")