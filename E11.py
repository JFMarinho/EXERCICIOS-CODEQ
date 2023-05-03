dados1=input("Digite a altura do pulo(1<=P<=5) e o numero de canos(2<=N<=100): ")
aux=dados1.split()
p=int(aux[0])
n=int(aux[1])
dados2=input("Digite a altura dos postes: ")
aux2=dados2.split()
altp=[int(x) for x in aux2]
conf=1
for i in range(n-1):
    if (i+1)>n:
        continue
    else:
        if altp[i]<altp[i+1]:
            if (altp[i]+p)<altp[i+1]:
                conf=0
        elif altp[i]>altp[i+1]:
            if (altp[i]-p)>altp[i+1]:
                conf=0
if(conf==0):
    print("GAME OVER")
else:
    print("YOU WIN")
