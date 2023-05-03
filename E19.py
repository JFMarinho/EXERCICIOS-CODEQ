c = int(input("Quantidade de casos de teste: "))
for i in range(c):
    n, m = map(int, input("Digite M e N: ").split())
    res = str(n ** m)
    print(len(res))