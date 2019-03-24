import matplotlib.pyplot as plt
import csv
import sys 

names = []
values = []
values_round = []

with open(sys.argv[1]) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for i in readCSV:
		print(i[0] + " : " + i[1])
		names.append(i[0])
		values.append(float(i[1]))
		values_round.append(round(float(i[1]), 2))
#data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
#names = list(data.keys())
#values = list(data.values())



#names = ['apples', 'oranges', 'lemons', 'limes']
#values = [10, 15, 5, 20]

#fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

fig, ax = plt.subplots()


plt.subplots_adjust(bottom=0.32, right=0.98, top=0.93, left=0.09)
rects = ax.bar(names, values, color=['whitesmoke', 'silver', 'gray', 'black'], edgecolor='black')

#print(rects[0])
#ax.set_xticklabels(values)
plt.title(sys.argv[2])
plt.ylabel(sys.argv[3])
plt.xlabel('Configuracao da Execucao [N threads, Tam. Vetor, N Repeticoes]')

tam = 0.15 * (max(values) - min(values))
plt.ylim(min(values) - tam, max(values) + tam)
plt.xticks(rotation='vertical')

for i in range(0, len(values)):
	(X, Y) = rects[i].xy
	plt.text(x=X+0.04, y=values[i] + 0.02, s=values_round[i], size = 7)
#	print('x = ' + str(X) + ', y = ' + str(Y))

#barlist = plt.bar()
#barlist[0].set_color('r')

#plt.show()
plt.savefig('graph.png')
