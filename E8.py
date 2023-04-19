import math
valores=input("Digite A, B e C: ")
aux=valores.split()
a=float(aux[0])
b=float(aux[1])
c=float(aux[2])
delta= ((b**2)-(4*a*c))
if delta>0 and a!=0:
     r1= ((-b) + math.sqrt(delta))/(2*a)
     r2= ((-b) - math.sqrt(delta))/(2*a)
     print("R1 = {:.5f}".format(r1))
     print("R2 = {:.5f}".format(r2))
elif delta==0 and a!=0:
     r1= (-b) /(2*a)
     r2= (-b) /(2*a)
     print("R1 = {:.5f}".format(r1))
     print("R2 = {:.5f}".format(r2))
else:
   print("Impossivel calcular")