#!/usr/bin/env python

# Desafío: Escribe la función del logaritmo neperiano
# sin usar alguna librería o API, usando el lenguaje que quieras.

# (aunque en Python esto sería como hacer trampa)

# Nota:  no utilicé recursión porque esta operación excedía el 
# la profundidad máxima de recursión. Y no tenía ganas de cambiar eso

NON_INFINITE = 1000000

def my_range(i, stop, step = 1):
	l = []
	if step <= 0: step = 1
	while(i < stop):
		l.append(i)
		i += step
	return l

def taylor_seq(val, times, sum = True):
	if times <= 0:
		sum = True
		times = 1

	total = 0.0
	for i in my_range(times, NON_INFINITE):
		if sum: total += ((val-1)**i)/i
		else: total -= ((val-1)**i)/i
		sum = not sum
	return total

# Usando la función argumento de la targente hiperbólica.
# Aún más eficiente que la serie de Taylor.
def hyp_tan(val):
	total = 0.0
	for i in my_range(1, NON_INFINITE, 2):
		total += (1/i)*((val-1)/(val+1))**i
	return 2.0*total


def ln(x):
	return hyp_tan(x)

def main():
	print("ln(10): ", ln(10)) # ln(10): 2.3025850929940455

if __name__ == '__main__':
	main()
