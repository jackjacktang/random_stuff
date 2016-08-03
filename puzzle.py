import numpy as np
import scipy

def check_digit(number,j):
	temp = list(map(int, number))
	count1 = temp.count(j)
	count2 = temp[j]
	print('digit: %d |count1: %d count2: %d' % (j,count1, count2))
	if (count1 == count2):
		return True
	else:
		return False


def main():
	flag = True
	for i in range (1000000000,9999999999):
		# print(i)
		temp = str(i)
		for j in range (0,10):
			if check_digit(temp,j) != True:
				flag = False
				break
			else:
				flag = True
		if (flag == True):
			print('FOUND: %d' % i);

if __name__ == "__main__":
    main()

