import random
import time
import math
import numpy as np

random.seed(53)

def decode(matrix):
    # Converter o arquivo numa array multi dimensional e criar uma array com os pontos de entrega.
    points = []
    positions = {}
    newmatrix = matrix[:]
    del (newmatrix[0:1])
    for index, item in enumerate(newmatrix):
        newmatrix[index] = item.split()
        for i, k in enumerate(newmatrix[index]):
            if k == 'R':
                positions["{}".format(k)] = index, i
            elif k != '0' and k != 'R':
                points.append(k)
                positions["{}".format(k)] = index, i
    return points, positions

def initialpop(points):
    pop = []
    while len(pop) <= 100:
        l1 = random.sample(points, len(points))
        # if l1 not in pop:
        pop.append(l1)
    return pop

# Funcao que calcula a distancia entre dois pontos "pontoa" e "pontob", levando em conta o dicionario que contem as posicoes de cada ponto
def distanceTwoPoints(pointa, pointb, dictionary):
    for i in dictionary:
        if i == pointa:
            pointaposition = list(dictionary["{}".format(i)])
    for i in dictionary:
        if i == pointb:
            pointbposition = list(dictionary["{}".format(i)])
    distance = abs(pointaposition[0] - pointbposition[0]) + abs(pointaposition[1] - pointbposition[1])
    return distance

def alldistances(points,dictionary):
    alldistances = {}
    points.append("R")
    for i,k in enumerate(points):
        for j in points[:i]+points[i+1:]:
            alldistances["{}".format(k+j)] = distanceTwoPoints(k,j,dictionary)
    return alldistances

# Funcao que calcula a distancia total, quando dada a permutacao, a posicao na lista e o dicionario de posicoes
def cal_pop_fitness(perm, distances):
    totalDistance = distances["{}".format("R"+perm[0])]
    for i in range(len(perm)-1):
        totalDistance += distances["{}".format(perm[i]+perm[i+1])]
    totalDistance += distances["{}".format(perm[len(perm)-1]+"R")]

    return totalDistance

# Considerando a lista com todas as permutacoes e o dicionario que contem as posicoes, a funcao calcula a distancia total de todas as permutacoes
def allFitnesses(pop, dictionary):
    popfitness = []
    for i, j in enumerate(pop):
        popfitness.append([j,cal_pop_fitness(pop[i],dictionary)])
    return popfitness

def tournament(popfitness):
    indexes = [random.randint(0,len(popfitness)-1) for x in range(2)]
    fighter1 = popfitness[indexes[0]]
    fighter2 = popfitness[indexes[1]]

    if fighter1[1] > fighter2[1]:
        return fighter2
    else:
        return fighter1


def crossover(parent1, parent2):
    if random.random() <= 0.9:
        split = int(len(parent1)/2)
        offspring1, offspring2 = parent1[0:split], parent2[0:split]

        for index, element in enumerate(parent2):
            if element not in offspring1:
                offspring1.append(element)
        for element in parent1:
            if element not in offspring2:
                offspring2.append(element)

        return offspring1, offspring2
    else:
        return parent1,parent2

def mutation(offspring):
    if random.random() <= 0.05:
        noffspring = offspring[:]
        split = random.randint(0,len(noffspring)-2)
        temp = noffspring[split]

        noffspring[split] = noffspring[split+1]
        noffspring[split+1] = temp
        return noffspring
    else:
        return offspring

def generatenewpop(pop,positions):
    newpop = []
    for i in range(50):
        p1, p2 = tournament(pop)[0], tournament(pop)[0]
        f1, f2 = (crossover(p1, p2))
        newpop.append(mutation(f1))
        newpop.append(mutation(f2))
    evaluatenewpop = allFitnesses(newpop,positions)
    best = evaluatenewpop[0]
    for element in evaluatenewpop:
        if element[1] < best[1]:
            best = element
    return evaluatenewpop, best

def geneticalgorithm(matrix):
    start = time.time()
    points,positions = decode(matrix)
    pop = initialpop(points)
    distances = alldistances(points,positions)
    pop = allFitnesses(pop,distances)
    bestlist = []

    for j in range(1000):
        pop,best = generatenewpop(pop,distances)
        bestlist.append(best)
    # while bestlist[len(bestlist)-1] != bestlist[len(bestlist)-2]:
    #     pop, best = generatenewpop(pop, distances)
    #     bestlist.append(best)
    end = time.time()



    return bestlist[len(bestlist)-1], end-start
