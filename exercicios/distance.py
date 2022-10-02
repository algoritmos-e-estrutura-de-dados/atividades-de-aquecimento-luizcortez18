import math
print("Informe os valores: ")
linha1 = input().split(" ")
print("Informe os valores: ")
linha2 = input().split(" ")
x1, y1 = linha1
x2, y2 = linha2

dis = math.sqrt(pow(float(x2)-float(x1),2)+pow(float(y2)-float(y1),2))

print(f"{dis: .4f}")