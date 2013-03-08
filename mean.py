import sys

def mean (numbers):
	sum=0
	for x in numbers:
		sum+=x
	return float(sum)/len(numbers)

numbers = []
for line in sys.stdin:
	numbers.append(int(line))
print mean(numbers)
