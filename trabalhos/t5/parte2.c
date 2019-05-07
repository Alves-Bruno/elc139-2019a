//
//  Este programa MPI tem um erro!
//  Identifique este erro e corrija-o para que 2 processos
//  possam trocar mensagens.
//
//  Uso: mpirun -np 2 <prog>
//
#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{
   int numtasks, rank, dest, tag, source, rc;
   int inmsg, outmsg = 100;
   MPI_Status stat;

   tag = 10;

   MPI_Init(&argc,&argv);
   MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);

   if (rank == 0) {
      dest = 1;
      source = dest;
      outmsg++;
      rc = MPI_Send(&outmsg, 1, MPI_INT, dest, tag, MPI_COMM_WORLD);
      printf("[%d] enviou mensagem para processo [%d]...\n", rank, dest);

   }
   else if(rank != 0 && rank < numtasks - 1) {
      dest = rank + 1;
      source = rank - 1;
      rc = MPI_Recv(&inmsg, 1, MPI_INT, source, tag, MPI_COMM_WORLD, &stat);
      printf("[%d] recebeu mensagem do processo [%d]...\n", rank, source);
      outmsg = inmsg + 1;
      rc = MPI_Send(&outmsg, 1, MPI_INT, dest, tag, MPI_COMM_WORLD);
      printf("[%d] enviou mensagem para processo [%d]...\n", rank, dest);
   }
   else{
           source = rank - 1;
           rc = MPI_Recv(&inmsg, 1, MPI_INT, source, tag, MPI_COMM_WORLD, &stat);
           printf("[%d] recebeu mensagem do processo [%d]. Valor final: %d\n", rank, source, inmsg);

   }

   MPI_Finalize();
}
