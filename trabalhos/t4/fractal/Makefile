all:
	g++ --std=c++0x -fopenmp fractalpar1.cpp -o fractalpar1
	g++ --std=c++0x -fopenmp fractalpar2.cpp -o fractalpar2
	g++ --std=c++0x -fopenmp fractalpar3.cpp -o fractalpar3
	g++ --std=c++0x fractal_serial.cpp -o fractal_serial
serial:
	g++ --std=c++0x fractal_serial.cpp -o fractal_serial
clean:
	rm fractal*.bmp
	rm fractalpar1
	rm fractalpar2
	rm fractalpar3
	rm fractal_serial
