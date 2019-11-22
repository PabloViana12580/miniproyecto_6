#Miniproyecto 6 
#Ana lucia Diaz Leppe 
#Pablo Viana Vidal
import numpy as np
from itertools import combinations

#Funcion fitness para el problema 1
def funcion_1(x1, x2):
	return 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2

#condicion para el genoma
def condicion_1(x1, x2):
	if x1 + 2*x2 <= 30:
		return True
	else:
		return False

#Mediante numeros aleatorios obtenemos nuestra población inicial
population = []
cont = 0 

for x in range(10000):
	num1 = np.random.randint(1,30)
	num2 = np.random.randint(1,30)
	if condicion_1(num1,num2) == True:
		a = np.array([num1,num2])
		population.append(a)

end_criteria = []

for y in population:
	fit1 = funcion_1(y[0],y[1])
	end_criteria.append(fit1)

end_criteria.sort(reverse=True)
max_fit = end_criteria[0]

while(True):

	if cont == 1000:
		print("Los valores para las variables x1, x2 que hacen el maximo en la funcion son:")
		print(population[0])
		print(max_fit)
		break

	#Evaluamos cada uno de los cromosomas en la funcion fitness
	fitness_score = []

	for y in population:
		fit = funcion_1(y[0],y[1])
		fitness_score.append(fit)


	#Ordenamos los valores y escogemos los dos cromosomas con mas alto punteo en la función fitness
	fitness = list.copy(fitness_score)
	fitness_score.sort(reverse=True)

	#Utilizamos un limite en la funcion fitness como criterio de finalización
	if fitness_score[0] > max_fit:
		max_fit = fitness_score[0]
	elif fitness_score[0] == max_fit:
		cont += 1

	#Usamos los indices para encontrar los cromosomas elite
	indx1 = fitness.index(fitness_score[0])
	indx2 = fitness.index(fitness_score[1])

	father = population[indx1]
	mother = population[indx2]

	fathermother = np.concatenate((father, mother))

	#Realizamos cross-over entre el padre y la madre
	children = combinations(fathermother,2)

	population = []

	population.append(father)
	population.append(mother)

	for i in list(children):
		arr = np.array(i)
		#Realizamos una mutación al azar 
		rand_pos = np.random.randint(0,2)
		rand_prob = np.random.uniform()

		if rand_prob > 0.80:
			arr[rand_pos] += 1

		population.append(arr)
