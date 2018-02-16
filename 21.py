def d(num):
	temp = 0
	for i in range(1,num):
		if num % i == 0:
			temp += i
	return temp

allSum = 0

for x in range(1,10001):
	amb = d(x)
	if x == d(amb)  and x != amb:
		allSum += x
	
print(allSum)
