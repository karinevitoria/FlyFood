import random
#
#
# def crossover(parent1, parent2):  #cruzamento realizado por PMX
#     break_point = randint(1, len(parent1)-1)
#     backup = parent2[:]
#     offspring = []
#
#     for child in range(2):
#         for point in range(break_point):
#             if parent1[point] != parent2[point]:
#                 temp = parent2[point]
#                 parent2[point] = parent1[point]
#
#                 for change_point in range(point+1, len(parent2)):
#                     if parent2[point] == parent2[change_point]:
#                         parent2[change_point] = temp
#                         break
#
#         offspring.append(parent2)
#         parent2 = parent1
#         parent1 = backup
#
#     return offspring
#
# print(crossover([1,2,3,4],[3,2,1,4]))

# def crossover(pai1,pai2):
#     pares = []
#
#     ## define o indice do corte que será feito nos pais originais
#     corte1 = random.randint(2,(len(pai1)-1))
#     # corte2 = random.randint((corte1), (len(pai1)-1))
#
#     ## caso o corte seja igual, ou contenha um pai inteiro, calcular outros valores de core
#     # while corte1 == corte2 or (corte1 == 0 and corte2 == len(pai1)):
#     #     corte1 = random.randint(0, (len(pai1)))
#     #     corte2 = random.randint((corte1), (len(pai1)))
#
#     filho1,filho2 = [],[]
#
#     for i in range(len(pai1)):
#         if i < corte1:
#             filho1.append(None)
#             filho2.append(None)
#         elif i >= corte1:
#             filho1.append(pai2[i])
#             filho2.append(pai1[i])
#     ## é feita uma cópia dos pais, mas é trocado os valores que estão dentro do corte
#
#
#     for elemento in pai1[corte1:]:
#         for elemento2 in pai2[corte1:]:
#             if elemento != elemento2 and ([elemento2,elemento] not in pares):
#                 pares.append([elemento, elemento2])
#
#     for indice,numero in enumerate(pai1):
#         if numero not in filho1:
#             if filho1[indice] == None:
#                 filho1[indice] = numero
#             else:
#                 for par in pares:
#                     if numero in par:
#                         paradequado = par
#                 nindice = pai1.index(paradequado[1])
#                 filho1[nindice] = numero
#     for indice2,numero2 in enumerate(pai2):
#         for i in range(len(filho2)):
#             if numero2 not in filho2:
#                 if filho2[indice2] == None:
#                     filho2[indice2] = numero2
#                 else:
#                     for par in pares:
#                         if numero2 in par:
#                             paradequado = par
#                     nindice2 = pai2.index(paradequado[0])
#                     filho2[nindice2] = numero2
#     return filho1, filho2, corte1,pares

# ## selection by ranking
#     ranking = []
#     popfitness = [popfitness[i][1] for i in range(len(popfitness))]
#     orderedlist = quicksort(popfitness)
#     for i in range(len(orderedlist)):
#         ranking.append(1/(i+2))
#
#     cumulativeTotal = 0.0
#     cumulativeProportions = []
#     for proportion in ranking:
#         cumulativeTotal += proportion;
#         cumulativeProportions.append(cumulativeTotal)
#         if cumulativeTotal >= 1:
#             break
#
#     selectedvalue = random.random()
#
#     for i in range(len(cumulativeProportions)):
#         value = cumulativeProportions[i]
#         if value >= selectedvalue:
#             orderedlist[i]
#
# def quicksort(v):
#     if len(v) <= 1:
#         return v
#     less, equal, greater = [],[],[]
#     pivot = v[0]
#     for x in v:
#         if x < pivot:
#             less.append(x)
#         elif x == pivot:
#             equal.append(x)
#         else:
#             greater.append(x)
#     return quicksort(less) + equal + quicksort(greater)

# selection by the roulette wheel

# roulette, normalizedProportions, onlyfitnesses, cosxlist = [], [], [], []
# for i, j in enumerate(popfitness):
#     onlyfitnesses.append(popfitness[i][1])
# minfitness = min(onlyfitnesses)
# for i in range(0, len(popfitness)):
#     cosx = abs((math.cos(((math.pi / 2) * (popfitness[i][1] - minfitness) * (180 / math.pi)))) * 100)
#     cosxlist.append(cosx)
# for cos in cosxlist:
#     normalizedProportions.append(cos / np.sum(cosxlist))
# cumulativeProportions = []
# cumulativeTotal = 0.0
#
# for proportion in normalizedProportions:
#     cumulativeTotal += proportion * 100;
#     cumulativeProportions.append(cumulativeTotal)
#
# selectedvalue = random.random()
#
# for i in range(len(cumulativeProportions)):
#     value = cumulativeProportions[i]
#     if value >= selectedvalue:
#         return popfitness[i]

#
# def hill_climb(dominio,funcao_custo):
#     solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
#     while True:
#         vizinhos = []
#         for i in range(len(dominio)):
#             if solucao[i] > dominio[i][0]:
#                 if solucao[i] != dominio[i][1]:
#                     vizinhos.append(solucao[0:i] + solucao)


# [aptd.append(x) for x in data[x][1]]

#
# def roulette(popfitness):
#     roulette, normalizedProportions, onlyfitnesses, cosxlist = [], [], [], []
#     worst = 0
#     for i, j in enumerate(popfitness):
#         onlyfitnesses.append(popfitness[i][1])
#         if j[1] > worst:
#             worst = j[1]
#     for index,element in enumerate(onlyfitnesses):
#         onlyfitnesses[index] = worst - element
#     minfitness = min(onlyfitnesses)
#     for i in range(0, len(popfitness)):
#         cosx = abs((math.cos(((math.pi / 2) * (popfitness[i][1] - minfitness) * (180 / math.pi)))) * 100)
#         cosxlist.append(cosx)
#     for cos in cosxlist:
#         normalizedProportions.append(cos / np.sum(cosxlist))
#     cumulativeProportions = []
#     cumulativeTotal = 0.0
#
#     for proportion in normalizedProportions:
#         cumulativeTotal += proportion * 100
#         cumulativeProportions.append(cumulativeTotal)
#
#     selectedvalue = random.random()
#
#     for i in range(len(cumulativeProportions)):
#         value = cumulativeProportions[i]
#         if value >= selectedvalue:
#             return popfitness[i]
#
