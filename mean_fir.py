import sys

sum=0
n=0

for num in sys.stdin:
<<<<<<< HEAD
	sum+=float(num)
=======
	sum+=float(sum)
>>>>>>> 8274ced70b58fefeb346db596ec01e537ddb67d6
	n+=1

print sum/n
