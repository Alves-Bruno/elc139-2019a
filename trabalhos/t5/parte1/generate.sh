#!/bin/bash
cd 1_mil
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 1.000 - MPI" "SPEED UP"
cd ..

cd 10_mil
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 10.000 - MPI" "SPEED UP"
cd ..

cd 100_mil
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 100.000 - MPI" "SPEED UP"
cd ..

cd 1_milhao
python ../generate_graph.py result_speedup.csv "SPEED UP com vetor de tamanho 1.000.000 - MPI" "SPEED UP"
cd ..
