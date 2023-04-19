idade=int(input("Idade em dias: "))
anos=idade/365
meses= (idade%365)/30
dias= (idade%365)%30
print(str(int(anos))+" Anos")
print(str(int(meses))+" Meses")
print(str(dias)+" Dias")