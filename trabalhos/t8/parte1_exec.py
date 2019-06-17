import sys
import os
import subprocess

repeat = 10
frames_sizes = [100, 200, 300, 400]
width_sizes = [1024]
csv_file = open("parte1_times.csv","w+")

#os.system('rm parte1.csv')
#cmd = "smpirun -np " + str(procs) + " -hostfile cluster_hostfile.txt -platform cluster_crossbar.xml ./exe_sr_bcast --cfg=smpi/host-speed:25200000000"
#result = subprocess.check_output(cmd, shell=True)

print('exec type, wave time (s), cuda time (s)')
csv_file.write('exec type, wave time (s), cuda time (s)\n')

for width in width_sizes:
  for frame in frames_sizes:
    wave_sum_time = 0.00
    cuda_sum_time = 0.00
    for i in range(0, repeat):
      cmd_wave = './wave ' + str(width) + ' ' + str(frame)
      cmd_cuda = './wavecuda1 ' + str(width) + ' ' + str(frame)
      #print(cmd_wave)
      #print(cmd_cuda)
      wave_time = subprocess.check_output(cmd_wave, shell=True)
      cuda_time = subprocess.check_output(cmd_cuda, shell=True)
      wave_sum_time = wave_sum_time + float(wave_time)
      cuda_sum_time = cuda_sum_time + float(cuda_time)

    sys.stdout.write('w='+str(width) + ' f='+ str(frame) + ', ' + str(wave_sum_time/repeat) + ', ' + str(cuda_sum_time/repeat) + '\n')
    csv_file.write('w='+str(width) + ' f='+ str(frame) + ', ' + str(wave_sum_time/repeat) + ', ' + str(cuda_sum_time/repeat) + '\n')

csv_file.close()
