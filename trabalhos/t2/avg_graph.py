import matplotlib.pyplot as plt
import csv
import sys 

Mixed_names = []
Mixed_values = []
Mixed_values_round = []

names = []
for i in range(0,160):
	names.append(str(i))
values = []
values_round = []

with open(sys.argv[1]) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for i in readCSV:
		if i[0] != "tool":
			print(i[0] + " : " + i[1])
			#names.append(i[0] + " " + i[1] + " " + i[2] + " " + i[3])
			values.append(float(i[4])/1000)
			values_round.append(round(float(i[4]), 2))


for i in range(0, len(values)/2):
	Mixed_values.append(values[i])
	Mixed_values.append(values[len(values)/2 + i])
	Mixed_names.append(names[i])
	Mixed_names.append(names[len(values)/2 + i])
	Mixed_values_round.append(values_round[i])
	Mixed_values_round.append(values_round[len(values)/2 + i])



fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0][0].bar(Mixed_names[0:40], Mixed_values[0:40], color=['whitesmoke', 'black'], edgecolor='black')
ax[0][1].bar(Mixed_names[40:80], Mixed_values[40:80], color=['whitesmoke', 'black'], edgecolor='black')
ax[1][0].bar(Mixed_names[80:120], Mixed_values[80:120], color=['whitesmoke', 'black'], edgecolor='black')
ax[1][1].bar(Mixed_names[120:160], Mixed_values[120:160], color=['whitesmoke', 'black'], edgecolor='black')


##fig, ax = plt.subplots()


##plt.subplots_adjust(bottom=0.32, right=0.98, top=0.93, left=0.09)
##rects = ax.bar(Mixed_names, Mixed_values, color=['whitesmoke', 'black'], edgecolor='black')

#print(rects[0])
#ax.set_xticklabels(values)

fig.suptitle(sys.argv[2], fontsize=16)
ax[0][0].set_title("1.000")
ax[0][1].set_title("10.000")
ax[1][0].set_title("100.000")
ax[1][1].set_title("1.000.000")

ax[0][0].set_ylabel('10^(-1) segundos')
ax[1][0].set_ylabel('10^(-1) segundos')

#ax[1][0].set_xlabel('Legenda: Branco - Pthread, Preto - OpenMP')
plt.text(x=-40, y=-2000, s= 'Legenda: Branco - Pthread, Preto - OpenMP', size = 12)

##plt.ylabel(sys.argv[3])
##plt.xlabel('Configuracao da Execucao [N threads, Tam. Vetor, N Repeticoes]')

##tam = 0.15 * (max(values) - min(values))
##plt.ylim(min(values) - tam, max(values) + tam)
##plt.xticks(rotation='vertical')



#for i in range(0, len(values)):
#	(X, Y) = rects[i].xy
#	plt.text(x=X+0.04, y=Mixed_values[i] + 0.02, s=Mixed_values_round[i], size = 7)
#	print('x = ' + str(X) + ', y = ' + str(Y))

#barlist = plt.bar()
#barlist[0].set_color('r')

ax[0][0].tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

ax[0][1].tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
ax[1][0].tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
ax[1][1].tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off


#plt.show()
plt.savefig('graph.png')
