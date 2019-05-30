import sys
import os
import subprocess

repeat = 50
sizes = [16, 32, 64, 128, 256]

os.system('rm parte1.csv')
os.system('echo "procs, avg time (msec)" >> parte1.csv')

for procs in sizes:
    media = 0.0
    sum = 0.0

    for i in range(0, repeat):
        cmd = "smpirun -np " + str(procs) + " -hostfile cluster_hostfile.txt -platform cluster_crossbar.xml ./exe_sr_bcast --cfg=smpi/host-speed:25200000000"
        result = subprocess.check_output(cmd, shell=True)
        sum = sum + float(result)

    media = sum/repeat
    os.system('echo "' + str(procs) + ',' + str(media) + '" >> parte1.csv')


os.system('echo "procs, avg time (usec)" >> parte1.csv')

for procs in sizes:
    media = 0.0
    sum = 0.0
    valores = []
    for i in range(0, repeat):
        cmd = "smpirun -np " + str(procs) + " -hostfile cluster_hostfile.txt -platform cluster_crossbar.xml ./exe_bcast_nativo --cfg=smpi/host-speed:25200000000"
        result = subprocess.check_output(cmd, shell=True)
        sum = sum + float(result)
        valores.append(float(result))

    media = sum/repeat
    os.system('echo "' + str(procs) + ',' + str(media) + '" >> parte1.csv')
