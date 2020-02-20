from sys import *

bb = 0
bl = 0
bd = 0
scores = []

lbooks = 0
processt = 0
bperday = 0
books = []
nrb = 0
l1 = []
l2 = []
nr = 0
l3 = []


def main():
	#input:
	bb = int(input())
	bl = int(input())
	

	bd = int(input())	
	#general:
	for i in range(0, bb):
		temp = int(input())
		scores.append(temp)
		
	#just for libray i:
	for i in range(0, bl):
		
		lbooks = int(input())
		processt = int(input())
		bperday = int(input())
		nr = lbooks
		nrb = int(processt + lbooks / bperday)
		for j in range(0, lbooks):
			temp1 = int(input())
			books.append(temp1)
		l1.append(bl-i-1)
		l2.append(nrb)
		if nrb >= nr :
			lbooks = lbooks -1
		l3.append(lbooks)
		
	#outputs:
	print('\n\n')		
	print(bl)
	print(l1)
	#print(l2) useless
	print(l3)
	l3.reverse()
	#scores.reverse() maybe ?
	for i in range(0, l1[0]+1):
		for k in range(0,l3[i]):
			print(scores[k], end=' ')
		print('\n')
			
if __name__ == '__main__' :
	main()			


'''
Example input data:
6
2
7
1
2
3
6
5
4
5
2
2
0
1
2
3
4
4
3
1
3
2
5
0

'''
		
