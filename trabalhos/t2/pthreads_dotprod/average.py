import csv
import sys


print('tool,nthreads,size,repetitions,usec')

with open(sys.argv[1]) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	linhas = []
	for row in readCSV:
		linhas.append(row);
        #print(row[0])
        #print(row[0],row[1])

	#print(readCSV[0])
	#sum = 0
	for i in range(1, 441, 22):
		sum = 0
		#print(linhas[i], end=', ');
		info = (linhas[i][0]).split(' ')
		print('Pthreads,' + info[1] + ',' + info[2] + ',' + info[3], end=',')
		#for num in range(19, 32):
		#	print(linhas[i][0][num])
		lin = i
		for lin in range(i + 1, i + 1 + 20):
			#print(linhas[lin][1])
			only_num = (linhas[lin][1]).split(' ')
			#print(only_num[1])
			sum = sum + float(only_num[1])

		print(sum/20)
