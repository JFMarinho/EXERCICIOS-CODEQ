p,j1,j2,r,a=map(int, input("Digite p,j1,j2,r,a: ").split())
soma=j1+j2
if not r:
    if (soma%2==0 and p==1) or (soma%2==1 and p==0):
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")
else:
    if a:
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")