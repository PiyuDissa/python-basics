# dict(dictionary) - mapping of keys to values
# {k1: v1, k2: v2}

tel = {'piyu': 712, 'lahiru': 923}
tel['piyu'] = 333
tel['amma'] = 444

print(tel)
print(tel['piyu'])
print(tel.keys())
print(tel.values())
print(tel.items())

for key,values in tel.items():
	print(key, values)