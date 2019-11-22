#Miniproyecto 6 
#Ana lucia Diaz Leppe 
#Pablo Viana Vidal
import numpy as np
from itertools import combinations

#Funcion fitness para el problema 1
def funcion_1(x1, x2):
	return 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2

#Funcion fitness para el problema 2
def funcion_2(x1, x2):
	return 3*x1 + 5*x2

#Función fitness para el problema 3 
def funcion_3(x1,x2):
	return 5*x1 - x1**2 + 8*x2 - 2*x2**2

#condicion para el problema 1
def condicion_1(x1, x2):
	if x1 + 2*x2 <= 30:
		return True
	else:
		return False

#Condicion para el problema 2
def condicion_2(x1,x2):
	if 3*x1 + 2*x2 <= 18:
		return True
	else:
		return False

def condicion_3(x1,x2):
	if 3*x1 + 2*x2 <= 6:
		return True
	else:
		return False

def ejercicio_1():
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
			print("\n-------------------- EJERCICIO 1 --------------------")
			print("para la funcion: 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2 ")
			print("Los valores para las variables x1, x2 que hacen el maximo son:")
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

			if condicion_1(arr[0],arr[1]) == True:
				population.append(arr)

def ejercicio_2():
	#Mediante numeros aleatorios obtenemos nuestra población inicial
	population = []
	cont = 0 

	for x in range(10000):
		num1 = np.random.randint(0,5)
		num2 = np.random.randint(0,6)
		if condicion_2(num1,num2) == True:
			a = np.array([num1,num2])

			population.append(a)

	end_criteria = []

	for y in population:
		fit1 = funcion_2(y[0],y[1])
		end_criteria.append(fit1)

	end_criteria.sort(reverse=True)
	max_fit = end_criteria[0]

	while(True):

		if cont == 1000:
			print("\n-------------------- EJERCICIO 2 --------------------")
			print("para la funcion: 3*x1 + 5*x2 ")
			print("Los valores para las variables x1, x2 que hacen el maximo son:")
			print(population[0])
			print(max_fit)
			break

		#Evaluamos cada uno de los cromosomas en la funcion fitness
		fitness_score = []

		for y in population:
			fit = funcion_2(y[0],y[1])
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

			if condicion_2(arr[0],arr[1]) == True:
				population.append(arr)

def ejercicio_3():
	#Mediante numeros aleatorios obtenemos nuestra población inicial
	population = []
	cont = 0 

	for x in range(10000):
		num1 = np.random.randint(0,6)
		num2 = np.random.randint(0,6)
		if condicion_3(num1,num2) == True:
			a = np.array([num1,num2])

			population.append(a)

	end_criteria = []

	for y in population:
		fit1 = funcion_3(y[0],y[1])
		end_criteria.append(fit1)

	end_criteria.sort(reverse=True)
	max_fit = end_criteria[0]

	while(True):

		if cont == 1000:
			print("\n-------------------- EJERCICIO 3 --------------------")
			print("para la funcion: 5*x1 - x1**2 + 8*x2 - 2*x2**2 ")
			print("Los valores para las variables x1, x2 que hacen el maximo son:")
			print(population[0])
			print(max_fit)
			break

		#Evaluamos cada uno de los cromosomas en la funcion fitness
		fitness_score = []

		for y in population:
			fit = funcion_3(y[0],y[1])
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

			if condicion_3(arr[0],arr[1]) == True:
				population.append(arr)

ejercicio_1()
ejercicio_2()
ejercicio_3()
