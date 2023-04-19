cod_ddd={
    '61':'Brasília',
    '71':'Salvador',
    '11':'São Paulo',
    '21':'Rio de Janeiro',
    '32':'Juiz de Fora',
    '19':'Campinas',
    '27':'Vitória',
    '31':'Belo Horizonte',
    '55':'Santa Maria'
}
ddd=input("Código DDD: ")
if ddd in cod_ddd:
    print("Região: "+cod_ddd[ddd])
else:
    print("Código DDD não encontrado")