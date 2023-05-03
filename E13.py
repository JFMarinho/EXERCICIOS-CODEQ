n=int(input("Quantidade de medidas (1 <N≤ 100): "))
temp=input("Medidas (-10000 ≤Hi≤ 10000): ")
aux=temp.split()
hi=[int(x) for x in aux]
anterior = "vale" if hi[0] < hi[1] else "pico"
for i in range(1, n):
    atual = "pico" if hi[i] > hi[i-1] else "vale"
    if i % 50 == 0 and atual != anterior:
        print(0)
        break
    elif atual == anterior and atual == "vale":
        print(0)
        break
    anterior = atual
else:
    print(1)
