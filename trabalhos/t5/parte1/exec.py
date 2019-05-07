import sys
import os

#os.system('echo "' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' ' + sys.argv[4] + '" >> ' + sys.argv[5])

#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

#tam_vet = 1000000
#tam_vet = 500 000
tam_vet = int(sys.argv[3])
for repeat in range(500, 3000, 500):
	for pot in range(0, 4):
		nthreads = pow(2,pot)

		os.system('echo "' + '" >> ' + sys.argv[2])
		os.system('echo "' + "mpiexec" + ' ' + str(nthreads) + ' ' + str(tam_vet/nthreads) + ' ' + str(repeat) + '" >> ' + sys.argv[2])
		for i in range(0, 20):
			print(sys.argv[1] + ' ' + str(nthreads) + ' ' + str(tam_vet/nthreads) + ' ' + str(repeat) + " >> " + sys.argv[2])
			os.system("mpiexec -np " + str(nthreads) + " " + sys.argv[1] + ' ' + str(nthreads) + ' ' + str(tam_vet/nthreads) + ' ' + str(repeat) + " >> " + sys.argv[2])
