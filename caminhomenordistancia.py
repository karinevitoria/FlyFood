import numpy as np
import matplotlib.pyplot as plt
import time

def caminhomininmo(lista):
    start = time.time()
    # Converter o arquivo numa array multi dimensional e criar uma array com os pontos de entrega.
    pontos = []
    del(lista[0:1])
    for index, item in enumerate(lista):
        lista[index] = item.split()
        for k in lista[index]:
            if k != '0' and k != 'R':
                pontos.append(k)



    # Todas as possibilidades de caminhos
    def permutacao(lista):
        if len(lista) == 0:
            return []
        if len(lista) == 1:
            return [lista]
        lista_auxiliar = []
        for indice in range(len(lista)):
            chave = lista[indice]
            lista_sem_chave = lista[:indice] + lista[indice + 1:]
            for p in permutacao(lista_sem_chave):
                lista_auxiliar.append([chave] + p)
        return lista_auxiliar


    def posicao(elemento, lista):
        for i, n in enumerate(lista):
            for c, j in enumerate(n):
                if j == elemento:
                    return i + 1, c + 1


    def todasposicoes(listapontos, lista):
        dictionary = {}
        for h in listapontos:
            dictionary["{}".format(h)] = posicao(h, lista)
        dictionary["R"] = posicao("R",lista)
        return dictionary


    def distanciaDoisPontos(pontoa, pontob, dicionario):
        for i in dicionario:
            if i == pontoa:
                posicaopontoa = list(dicionario["{}".format(i)])
            elif i == pontob:
                posicaopontob = list(dicionario["{}".format(i)])
        distancia = abs(posicaopontoa[0] - posicaopontob[0]) + abs(posicaopontoa[1] - posicaopontob[1])
        return distancia


    def distanciaTotal(listapermutada, nperm, dicionario):
        distanciaTotal = distanciaDoisPontos("R", listapermutada[nperm][0], dicionario)
        for i in range(len(listapermutada[nperm])-1):
            distanciaTotal += distanciaDoisPontos(listapermutada[nperm][i], listapermutada[nperm][i+1], dicionario)
        distanciaTotal += distanciaDoisPontos("R", listapermutada[nperm][len(listapermutada[nperm])-1], dicionario)
        return distanciaTotal


    def todasAsDistancias(listapermutada, dicionario):
        todasDistancias = []
        for i,j in enumerate(listapermutada):
            todasDistancias.append([j, distanciaTotal(listapermutada, i, dicionario)])
        return todasDistancias


    def menorCaminho(lista):
        listaAuxiliar = []
        for i,j in enumerate(lista):
            listaAuxiliar.append(lista[i][1])
        return lista[listaAuxiliar.index(min(listaAuxiliar))]


    menorCaminho1 = menorCaminho(todasAsDistancias(permutacao(pontos),todasposicoes(pontos, lista)))
    end = time.time()

    return menorCaminho1[0], todasposicoes(pontos,lista),end-start
