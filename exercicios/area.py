valores = map(float,input().split(" "))
a,b,c = valores
tri=0.5*a*c
cir=3.14159*(c*c)
tra=(a+b)/2*c
squa=b*b
rec=a*b
print(f"TRIANGULO: {tri: .3f}")
print(f"CIRCULO: {cir: .3f}")
print(f"TRAPEZIO: {tra: .3f}")
print(f"QUADRADO: {squa: .3f}")
print(f"RETANGULO: {rec: .3f}")