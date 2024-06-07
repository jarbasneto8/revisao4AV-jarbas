def maior(*numeros):
    maior_valor = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior_valor:
            maior_valor = numeros[i]
    print(maior_valor)

maior(1,2,3,4,5)
maior(4,7)
maior(100,1)