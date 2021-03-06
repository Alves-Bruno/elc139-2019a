import csv
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

wave_times = []
cuda_times = []
labels = []
rows = []
with open('parte1_times.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		aux = []
		aux.append(row[0])
		aux.append(row[1])
		aux.append(row[2])
		rows.append(aux)

	for row in rows[1:]:
		labels.append(row[0])
		wave_times.append(float(row[1]))
		cuda_times.append(float(row[2]))

#print(rows)
x_indexes = np.arange(len(labels))
width = 0.25

#plt.bar(x_indexes + width, cuda_times, width=width, color="#008fd5", label="Python")
#plt.bar(x_indexes, wave_times, width=width, color="#444444", label="All Devs")

plt.plot(x_indexes, wave_times, color="#444444", label="wave")
plt.plot(x_indexes, cuda_times, color="#008fd5", label="CUDA_wave")


plt.legend()

plt.xticks(ticks=x_indexes, labels=labels)
plt.title("Wave.cpp X CUDA_wave")
plt.xlabel("Tipo de Execucao")
plt.ylabel("Tempo de Exec. (s)")

plt.tight_layout()

fig = plt.gcf()
fig.set_size_inches(10, 8)
fig.savefig('parte1.png', dpi=100)
