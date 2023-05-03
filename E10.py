inter=0
gremio=0
empates=0
continuar=1
while (continuar==1):
    placar=input("Placar do jogo (inter x gremio): ")
    aux=placar.split()
    inte=int(aux[0])
    gre=int(aux[1])
    if(inte>gre): 
        inter+=1
    elif(inte==gre):
        empates+=1
    else:
        gremio+=1
    continuar=int(input("Novo grenal (1-sim/2-não): "))
print(str(inter+gremio+empates)+" jogos")
print("inter: "+str(inter))
print("Empates: "+str(empates))
print("Gremio: "+str(gremio))