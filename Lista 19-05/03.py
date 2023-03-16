def preencher(lista = list()):
    while True:
        entrada = input(f"Insira um carácter para a lista:\n {lista}\n")
        if entrada.isalnum() and len(entrada) == 1 :
            lista.append(entrada)
        else:
            break

    print("Lista preenchida.")

#Preencher duas listas com caracteres e comparar as duas
listaA = []
listaB = []

preencher(listaA)
preencher(listaB)

diferAB = list(set(listaA) - set(listaB))

diferBA = list(set(listaB) - set(listaA))

interseccao = list(set(listaA) & set(listaB))

uniao = list(set(listaA) | set(listaB))

print(f"-lista A:{listaA}  \n-lista B:{listaB} \n-A-B:{diferAB} \n-B-A:{diferBA} \n-Intersecção:{interseccao} \n-União:{uniao} ")