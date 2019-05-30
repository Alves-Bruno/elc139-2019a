// Adaptado de www.mpitutorial.com
// Exemplo de implementação do MPI_Bcast usando MPI_Send e MPI_Recv

#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>

int main(int argc, char** argv) {

  double start_time, end_time;
  int myrank;    // "rank" do processo
  int p;         // numero de processos
  int root;      // rank do processo root

  // MPI_Init deve ser invocado antes de qualquer outra chamada MPI
  MPI_Init(&argc, &argv);
  // Descobre o "rank" do processo
  MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
  // Descobre o numero de processos
  MPI_Comm_size(MPI_COMM_WORLD, &p);

  int data;     // dado a ser enviado
  root = 0;     // define o rank do root

  if (myrank == root) {
        start_time =  MPI_Wtime();
    data = 100;  // atribui um valor para ser enviado
    // printf("Processo %d (root) realizando broadcast do dado %d\n", root, data);
    // sr_bcast(&data, 1, MPI_INT, root, MPI_COMM_WORLD);
    MPI_Bcast(&data, 1, MPI_INT, root, MPI_COMM_WORLD);
  } else {
    MPI_Bcast(&data, 1, MPI_INT, root, MPI_COMM_WORLD);
    // printf("Processo %d recebendo dado %d do processo root\n", myrank, data);
  }

  MPI_Barrier(MPI_COMM_WORLD);

  if(myrank == root){

        end_time =  MPI_Wtime();
        printf("%f\n", (end_time - start_time)*1000);
  }
  MPI_Finalize();
  return 0;
}
