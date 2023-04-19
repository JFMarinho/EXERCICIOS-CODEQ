num=int(input("Numero do funcionario: "))
hrs=int(input("Horas trabalhadas: "))
vhrs=float(input("Valor por hora: "))
salario=hrs*vhrs
print("Number = "+str(num))
print("Salary = U$ {:.2f}".format(salario))