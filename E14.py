n=int(input("Numero de membros (1 ≤N≤ 105): "))
votos=input("Votos (1 para impeachment e 0 para não): ")
v=[int(x) for x in votos.split()]
cont0=0
cont1=0
for i in v[:n]:
    if i==1: cont1+=1
    elif i==0: cont0+=1
if cont1>=(n*.666):
    print("impeachment")
else:
    print("Não impeachment")