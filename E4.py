valores=input("Digite A, B e C: ")
dados=valores.split()
a=float(dados[0])
b=float(dados[1])
c=float(dados[2])
triangulo=a*c/2
circulo=2*3.14159*c
trapezio=(a+b)*c/2
quadrado=b*b
retangulo=a*b
print("Triangulo {:.3f}".format(triangulo))
print("Circulo {:.3f}".format(circulo))
print("Trapezio {:.3f}".format(trapezio))
print("Quadrado {:.3f}".format(quadrado))
print("Retangulo {:.3f}".format(retangulo))