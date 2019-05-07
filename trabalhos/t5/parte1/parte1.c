#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#include <string.h>
#include "mpi.h"

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

  int source;         // "rank" do processo remetente
  int dest;           // "rank" do processo destinat�rio
  int tag = 0;        // "etiqueta" da mensagem
  char msg[100];      // a mensagem
  MPI_Status status;  // "status" de uma opera��o efetuada
  int myrank;         // "rank" do processo (0 a P-1)
  int p;              // n�mero de processos
  // MPI_Init deve ser invocado antes de qualquer outra chamada MPI
  MPI_Init(&argc, &argv);
  // Descobre o "rank" do processo
  MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
  // Descobre o n�mero de processos
  MPI_Comm_size(MPI_COMM_WORLD, &p);

if(myrank == 0){
        // Começa a contar o tempo antes das execuções paralelas
        start_time = wtime();
}

        dotdata_t dotdata;

        // Cria vetores
        dotdata.a = (double *) malloc(wsize*sizeof(double));
        fill(dotdata.a, wsize, 0.01);
        dotdata.b = (double *) malloc(wsize*sizeof(double));
        fill(dotdata.b, wsize, 1.0);
        dotdata.c = 0.0;
        dotdata.wsize = wsize;
        dotdata.repeat = repeat;

        int i, k;

        long offset = (long) myrank;
        double *a = dotdata.a;
        double *b = dotdata.b;
        wsize = dotdata.wsize;
        int start = 0;
        int end = wsize;
        double mysum;

        for (k = 0; k < dotdata.repeat; k++) {
           mysum = 0.0;
           for (i = start; i < end ; i++)  {
              mysum += (a[i] * b[i]);
           }
        }

        if(myrank == 0){

                for(source = 1; source < p; source++){
                        double sum_recv;
                        MPI_Recv(&sum_recv, 1, MPI_DOUBLE, source, tag, MPI_COMM_WORLD, &status);
                        dotdata.c += sum_recv;
                }
                dotdata.c += mysum;
                end_time = wtime(); // Para o contador.

//               printf("%f\n", dotdata.c);
               printf("%d thread(s), %ld usec\n", nthreads, (long) (end_time - start_time));
               free(dotdata.a);
               free(dotdata.b);

        }else{
                dest = 0;
                MPI_Send(&mysum, 1, MPI_DOUBLE, dest, tag, MPI_COMM_WORLD);
                free(dotdata.a);
                free(dotdata.b);
        }


MPI_Finalize(); // finaliza MPI

  return 0;
}
