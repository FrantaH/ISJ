#!/usr/bin/env python3

from collections import OrderedDict


def first_with_given_key(vals,key = lambda x:x):
	"""funkce pro vrácení správných prvků na základě zadaného klíče"""
	kes = map(key,vals)
	
	result_dict = OrderedDict()
	for indx, k in enumerate(kes):
		if k not in result_dict:
			result_dict[k] = vals[indx]
			yield vals[indx]
	

# first_with_given_key = lambda iter, key = lambda x:x : list(dict([( key(i), i) for i in iter[::-1]]).values())

"""print("moje")
print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))

print('([1], [2, 3], [5, 6, 7])')

print("moje")
print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))

print("([1], [2, 3], [5, 6, 7])")

print("moje")
print(tuple(first_with_given_key([[1],[2,3],[4],[1],[5,6,7],[8,9]], key = len)))
print("([1], [2, 3], [5, 6, 7])")"""
