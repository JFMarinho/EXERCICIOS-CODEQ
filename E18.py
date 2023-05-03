b=int(input("Bolinhas: "))
g=int(input("Galhos: "))
if b>=g/2:
    print("Amelia tem todas bolinhas!")
else:
    f=(g/2)-b
    print("Faltam "+ str(int(f)) + " Bolinha(s)")