print("Informe respectivamente quanto o carro percorreu e seu consumo total de combustível")
valores=input().split(" ")
p,c=valores

resul= int(p)/float(c) 

print(f"{resul: .3f} km/l")