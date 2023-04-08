# Counter
from collections import Counter

print(Counter(['B','B','A','B','C','A','B',
			'B','A','C']))
	
print(Counter({'A':3, 'B':5, 'C':2}))
	
print(Counter(A=3, B=5, C=2))

# ---------------------------------------------------

# ChainMap	
from collections import ChainMap
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)	
print(c)

# ---------------------------------------------------