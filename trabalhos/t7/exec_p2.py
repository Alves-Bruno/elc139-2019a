import sys
import os
import subprocess

repeat = 20
sizes = [256]
tamanhos_vetor = [500, 1000, 1500, 2000]
latencias = ['1us', '5us', '10us']
larguras_de_banda = ['16000bps', '64000bps', '125Mbps']
echo1 = 'echo "'
echo2 = '" >> cluster_config.xml'

os.system('rm parte2.csv')
os.system('echo "config, avg time (msec)" >> parte2.csv')


for tam_vetor in tamanhos_vetor:
    for latencia in latencias:
        for bw in larguras_de_banda:

            os.system('rm cluster_config.xml')
            os.system(echo1 + "<?xml version='1.0'?>" + echo2)
            os.system(echo1 + '<!DOCTYPE platform SYSTEM \\"http://simgrid.gforge.inria.fr/simgrid/simgrid.dtd\\">'+ echo2)
            os.system(echo1 + '<platform version=\\"4.1\\">'+ echo2)
            os.system(echo1 + '    <zone id=\\"AS0\\" routing=\\"Full\\">'+ echo2)
            os.system(echo1 + '        <cluster id=\\"my_cluster\\" prefix=\\"host-\\" suffix=\\".ufsm.br\\" radical=\\"0-255\\" speed=\\"1Gf\\" bw=\\"' + bw + '\\" lat=\\"' + latencia + '\\"/>' + echo2)
            os.system(echo1 + '    </zone>'+ echo2)
            os.system(echo1 + '</platform>'+ echo2)


            for procs in sizes:
                media = 0.0
                sum = 0.0

                for i in range(0, repeat):
                    cmd = "smpirun -np " + str(procs) + " -hostfile cluster_hostfile.txt -platform cluster_config.xml ./exe_avg " + str(tam_vetor) + " --cfg=smpi/host-speed:25200000000"
                    result = subprocess.check_output(cmd, shell=True)
                    sum = sum + float(result)

                media = sum/repeat
                os.system('echo "' + str(tam_vetor) + '_' + latencia + '_' + bw + ',' + str(media) + '" >> parte2.csv')
