for i in range(3, 101):
	flag = False
	if i == 4:
		continue
	for j in range(2, (int)(i/2)):
		if (i % j == 0):
			flag = True
	if flag == False: 
		print(i)

	
	
