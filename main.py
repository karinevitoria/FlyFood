import numpy as np
import matplotlib.pyplot as plt
from caminhomenordistancia import caminhomininmo

# lendo os conteudos dos arquivos
with open('exemplo1.txt') as f:
    matrix = f.readlines()
with open('exemplo2.txt') as f:
    matrix2 = f.readlines()
with open('exemplo3.txt') as f:
    matrix3 = f.readlines()
with open('exemplo4.txt') as f:
    matrix4 = f.readlines()
with open('exemplo5.txt') as f:
    matrix5 = f.readlines()
with open('exemplo6.txt') as f:
    matrix6 = f.readlines()


tamanho = [int(x) for x in matrix4[0].split()]

# calculando o menor caminho das matrizes de exemplo
retmatrix = caminhomininmo(matrix)
retmatrix2 = caminhomininmo(matrix2)
retmatrix3 = caminhomininmo(matrix3)
retmatrix4 = caminhomininmo(matrix4)
# retmatrix5 = caminhomininmo(matrix5)
# retmatrix6 = caminhomininmo(matrix6)

# função para substituir os pontos no melhor caminho pelos pontos (listados no dicionário)
def percursoNaMatrix(melhorCaminho, dicionario):
    melhorCaminho.insert(0,'R')
    melhorCaminho.append('R')
    lista_auxiliar = []
    for i,j in enumerate(melhorCaminho):
        for k in dicionario:
            if k == j:
                lista_auxiliar.append(list(dicionario["{}".format(k)]))


    return lista_auxiliar

# criando o percurso na matrix
labels = retmatrix4[0]
melhor_percurso = np.array(percursoNaMatrix(retmatrix4[0],retmatrix4[1]))

for i in range(len(retmatrix4[0])):
    label = labels[i]
    if i < len(retmatrix4[0])-1:
        plt.plot(
            np.array([melhor_percurso[i : i + 1, 1], melhor_percurso[i : i + 1, 1]]),
            np.array(
                [melhor_percurso[i : i + 1, 0], melhor_percurso[i + 1 : i + 2, 0]]
            ),
            "ko-",
            linewidth=2,
            markersize=10,
        )
        plt.plot(
            np.array(
                [melhor_percurso[i : i + 1, 1], melhor_percurso[i + 1 : i + 2, 1]]
            ),
            np.array(
                [melhor_percurso[i + 1 : i + 2, 0], melhor_percurso[i + 1 : i + 2, 0]]
            ),
            "ko-",
            linewidth=2,
            markersize=10,
        )
        plt.annotate(
            label,  # this is the text
            (
                melhor_percurso[i : i + 1, 1],
                melhor_percurso[i : i + 1, 0],
            ),  # these are the coordinates to position the label
            textcoords="offset points",  # how to position the text
            xytext=(10, 1),  # distance from text to points (x,y)
            ha="center",
            fontsize=14,
            fontname='Times New Roman'
        )  # horizontal alignment can be left, right or center
    else:
        plt.annotate(
            label,  # this is the text
            (
                melhor_percurso[i : i + 1, 1],
                melhor_percurso[i : i + 1, 0],
            ),  # these are the coordinates to position the label
            textcoords="offset points",  # how to position the text
            xytext=(10, 1),  # distance from text to points (x,y)
            ha="center",
            fontsize=14,
            fontname='Times New Roman'
        )  # horizontal alignment can be left, right or center
plt.title("Melhor percurso para a matriz com 8 pontos de entrega", fontsize=18, fontdict={'fontname':"Times New Roman"})
plt.xlabel("Coordenada X", fontsize=14, fontdict={'fontname':"Times New Roman"})
plt.ylabel("Coordenada Y", fontsize=14, fontdict={'fontname':"Times New Roman"})
plt.xticks([int(i) for i in range(tamanho[1]+1)],fontsize=14,fontname='Times New Roman')
plt.yticks([int(i) for i in range(tamanho[0]+1)],fontsize=14,fontname='Times New Roman')
plt.show()
print(retmatrix4[2])


# # Plot de experimentos (tempo e pontos de entrega)
# x = retmatrix[0], retmatrix2[0], retmatrix3[0], retmatrix4[0]
# y = retmatrix[1], retmatrix2[1], retmatrix3[1], retmatrix4[1]
# error = [0,0,0.002,0.1],[0,0.0003,0.002,0.1]
#
# # plt.plot(x, y)
# fig, ax = plt.subplots()
# ax.errorbar(x, y, yerr=error,mfc="blue", mec="green", ms=10, mew=4)
# plt.title('Tempo de execução', fontdict={'fontname': 'Times New Roman'})
# plt.xlabel('N° de pontos')
# plt.ylabel('Segundos')
# plt.xticks([4, 5, 6, 8, 10, 11])
# print(x,y)
#
# plt.show()