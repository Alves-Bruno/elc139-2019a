import os

testes = ["512 32", "512 64", "1024 32", "1024 64"]
num_threads = [2, 4]

for teste in testes:
	for repeat in range(0, 10):
		cmd = './' + 'fractal_serial' + ' ' + teste + ' >> ' + 'fractal_serial.csv'
		print(str(repeat) + ': ' + cmd)
#		os.system(cmd)


for teste in testes:
	for num_thread in num_threads:
		for i in range(0, 3):
			for repeat in range(0, 10):
				cmd = './' + 'fractalpar' + str(i+1) + ' ' + teste + ' ' + str(num_thread) + ' >> ' + 'fractalpar' + str(i+1) + '.csv'
				print(str(repeat) + ': ' + cmd)
#				os.system(cmd)

