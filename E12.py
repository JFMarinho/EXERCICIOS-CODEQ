t=int(input("Tipo de cha (1 ≤T≤ 4): "))
res=input("Digite a resposta de cada participante: ")
aux=res.split()
respostas=[int(x) for x in aux]
cont=0
for i in respostas:
    if i==t: cont+=1
print("Respostas corretas: "+ str(cont))