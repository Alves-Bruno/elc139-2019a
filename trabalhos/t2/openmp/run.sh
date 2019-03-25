#!/bin/bash
mkdir 1_mil
cd 1_mil
python ../exec.py ../ompsimple resultado.csv 1000
python3 ../average.py resultado.csv >> result_avg.csv
python3 ../speed_up.py resultado.csv >> result_speedup.csv
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 1.000 - OpenMP" "SPEED UP"
cd ..


mkdir 10_mil
cd 10_mil
python ../exec.py ../ompsimple resultado.csv 10000
python3 ../average.py resultado.csv >> result_avg.csv
python3 ../speed_up.py resultado.csv >> result_speedup.csv
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 10.000 - OpenMP" "SPEED UP"
cd ..

mkdir 100_mil
cd 100_mil
python ../exec.py ../ompsimple resultado.csv 100000
python3 ../average.py resultado.csv >> result_avg.csv
python3 ../speed_up.py resultado.csv >> result_speedup.csv
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 100.000 - OpenMP" "SPEED UP"
cd ..

mkdir 1_milhao
cd 1_milhao
python ../exec.py ../ompsimple resultado.csv 1000000
python3 ../average.py resultado.csv >> result_avg.csv
python3 ../speed_up.py resultado.csv >> result_speedup.csv
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 1.000.000 - OpenMP" "SPEED UP"
cd ..
