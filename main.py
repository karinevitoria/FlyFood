import numpy

from geneticalgorithm import geneticalgorithm
from geneticalgorithmwelitism import geneticalgorithmwelitism
from geneticalgorithmwelitism import distanceTwoPoints
from geneticalgorithmwelitism import decode
from bruteforce import caminhomininmo
import numpy as np
import matplotlib.pyplot as plt

# lendo os conteudos dos arquivos
with open('exemplos/matrices/exemplo1.txt') as f:
    matrix = f.readlines()
with open('exemplos/matrices/exemplo2.txt') as f:
    matrix2 = f.readlines()
with open('exemplos/matrices/exemplo3.txt') as f:
    matrix3 = f.readlines()
with open('exemplos/matrices/exemplo4.txt') as f:
    matrix4 = f.readlines()
with open('exemplos/matrices/exemplo5.txt') as f:
    matrix5 = f.readlines()
with open('exemplos/matrices/exemplo6.txt') as f:
    matrix6 = f.readlines()
with open('exemplos/matrices/exemplo7.txt') as f:
    matrix7 = f.readlines()
with open('exemplos/matrices/exemplo8.txt') as f:
    matrix8 = f.readlines()
with open('exemplos/matrices/exemplo9.txt') as f:
    matrix9 = f.readlines()
with open('exemplos/matrices/example10.txt') as f:
    matrix10 = f.readlines()

with open('exemplos/tsplib/a280.txt') as f:
    a280 = f.readlines()
with open('exemplos/tsplib/st80.txt') as f:
    st80 = f.readlines()


todasmatrizes = [matrix,matrix2,matrix3,matrix4,matrix5,matrix6]
## experimento 1

# print(geneticalgorithmwelitism(st80))


# matrix10copy = matrix10[:]

# gawe = [(x[1]) for x in geneticalgorithmwelitism(matrix10copy)[0]]
# ga = [(k[1]) for k in geneticalgorithm(matrix10)[0]]
# x = [x for x in range(len(ga))]

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, ga, color='tab:blue',label='sem elitismo')
# ax.plot(x, gawe, color='tab:orange',label='com elitismo')
# plt.title('Elitismo', fontdict={'fontname': 'Times New Roman'})
# plt.xlabel('Distância', fontdict={'fontname': 'Times New Roman'})
# plt.ylabel('Gerações', fontdict={'fontname': 'Times New Roman'})
# plt.xticks(fontname= 'Times New Roman')
# plt.yticks(fontname= 'Times New Roman')
# plt.legend()
# plt.show()


## experimento 2

def times30(matrix1):
    ga1, t1 = [],[]
    for x in range(30):
        l1, tx1 = matrix1
        ga1.append(l1[1]), t1.append(tx1)
    ga1 = numpy.sum(ga1)/30
    t1 = numpy.sum(t1)/30
    return ga1,t1
#
# y = caminhomininmo(matrix)[1], caminhomininmo(matrix2)[1], caminhomininmo(matrix3)[1], caminhomininmo(matrix4)[1], caminhomininmo(matrix5)[1], caminhomininmo(matrix6)[1]
y1 = []
x = []
#
for indice,matriz in enumerate(todasmatrizes):
    globals()['rese%s' % indice],globals()['tempe%s' % indice] = times30(geneticalgorithmwelitism(matriz))
    y1.append(globals()['tempe%s' % indice])
    x.append(globals()['rese%s' % indice])

#
# x = [4,5,6,8,10,11]

print(x,y1)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, y, color='tab:blue',label='força bruta')
# ax.plot(x, y1, color='tab:orange',label='algoritmo genético')
# plt.title('Tempo de execução', fontdict={'fontname': 'Times New Roman'})
# plt.xlabel('N° de pontos', fontdict={'fontname': 'Times New Roman'})
# plt.ylabel('Segundos', fontdict={'fontname': 'Times New Roman'})
# plt.xticks(fontname= 'Times New Roman')
# plt.yticks(fontname= 'Times New Roman')
# plt.legend()
# plt.show()