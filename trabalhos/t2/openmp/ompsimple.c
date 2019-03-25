#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

typedef struct
 {
   double *a;
   double *b;
   double c;
   int wsize;
   int repeat;
 } dotdata_t;

/*
 * Preenche vetor
 */
void fill(double *a, int size, double value)
{
   int i;
   for (i = 0; i < size; i++) {
      a[i] = value;
   }
}

/*
 * Tempo (wallclock) em microssegundos
 */
long wtime()
{
   struct timeval t;
   gettimeofday(&t, NULL);
   return t.tv_sec*1000000 + t.tv_usec;
}

int main(int argc, char **argv){

  int nthreads, wsize, repeat;
  long start_time, end_time;

  if ((argc != 4)) {
     printf("Uso: %s <nthreads> <worksize> <repetitions>\n", argv[0]);
     exit(EXIT_FAILURE);
  }

  nthreads = atoi(argv[1]);
  wsize = atoi(argv[2]);  // worksize = tamanho do vetor de cada thread
  repeat = atoi(argv[3]); // numero de repeticoes dos calculos (para aumentar carga)

  dotdata_t dotdata;

  // Cria vetores
  dotdata.a = (double *) malloc(wsize*nthreads*sizeof(double));
  fill(dotdata.a, wsize*nthreads, 0.01);
  dotdata.b = (double *) malloc(wsize*nthreads*sizeof(double));
  fill(dotdata.b, wsize*nthreads, 1.0);
  dotdata.c = 0.0;
  dotdata.wsize = wsize;
  dotdata.repeat = repeat;

  // Variavel que controla o offset
  int arg = -1;
  // Seta o número de threads de acordo com o argv[1] informado
  omp_set_num_threads(nthreads);

  // Começa a contar o tempo antes das execuções paralelas
  start_time = wtime();

  // Começo da execução paralela.
  #pragma omp parallel shared(dotdata, arg)
  {

    int i, k;

    // Simula o FOR que chamava as threads no código com pthreads.
    #pragma omp critical
    {arg++;}
    long offset = (long) arg;
    double *a = dotdata.a;
    double *b = dotdata.b;
    int wsize = dotdata.wsize;
    int start = offset*wsize;
    int end = start + wsize;
    double mysum;

    for (k = 0; k < dotdata.repeat; k++) {
       mysum = 0.0;
       for (i = start; i < end ; i++)  {
          mysum += (a[i] * b[i]);
       }
    }

    #pragma omp critical
    {dotdata.c += mysum;}

  } // fim da execução paralela
  end_time = wtime(); // Para o contador.

  // printf("%f\n", dotdata.c);
  printf("%d thread(s), %ld usec\n", nthreads, (long) (end_time - start_time));
  free(dotdata.a);
  free(dotdata.b);


  return 0;
}
