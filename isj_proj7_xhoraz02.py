#!/usr/bin/env python3

import collections

class log_and_count(object):
	"""třída pro vytvoření objektu u dekorátoru log_and_count a následné pamatování si argumentů k účelu využití při pozdějším volání funkce"""

	def __init__(self, key = None, counts = None):
		"""inicializace objektu: vytvoření interních proměnných pro argumenty a kontrole jejich zadání
		probímá u definice funkce s dekorátorem"""

		if (counts == None):
			print("chyba! musíte zadat argument counts!")
			exit(1)

		self.key = key
		self.counts = counts
	
	def __call__(self, old_function):
		"""vypsání zadaného popisu, přičtení do counteru a následné zavolání původní funcke
		probíhá při volání dekorované funkce"""

		def new_function(*args, **kwarg):
			"""funkce, která se volá místo dekorované funkce"""

			print("called " + old_function.__name__ + " with " + str(args) + " and " + str(kwarg) )
			if (self.key == None):
				self.key = old_function.__name__

			self.counts[self.key] += 1


			old_function(*args, **kwarg)		
		return new_function


my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
	return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
	return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
	return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)

# a vypíše postupně:
# called f1 with (2,) and {}
# called f2 with (2,) and {'b': 4}
# called f1 with () and {'a': 2, 'b': 4}
# called f2 with (4,) and {}
# called f2 with (5,) and {}
# called f3 with (5,) and {}
# called f3 with (5, 4) and {}

# a po:
print(my_counter)
# vypíše
# Counter({'basic function': 5, 'f3': 2})