dados=input("Digite a quantidade de competidores, a quantidade de folhas e a quantidade de folhas especiais: ").split()
c=int(dados[0])
p=int(dados[1])
f=int(dados[2])

if c * f <= p:
    print('S')
else:
    print('N')
