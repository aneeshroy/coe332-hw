def numtype(numbers):
	numtypes = []
	for i in numbers:
		if (i % 2 == 0):
			numtypes.append('even')
		else:
			numtypes.append('odd')
	return numtypes

numbers = [3,12,4,10,49,20,33,8,68,100]
numtypes = numtype(numbers)

for i in range (len(numbers)):
	print(numbers[i], " ", numtypes[i])



