* Nome: Bruno da Silva Alves.
* Nome da disciplina: Programação Paralela elc139-2019a

## Parte I: Pthreads

##### 1. Explique como se encontram implementadas as 4 etapas de projeto: particionamento, comunicação, aglomeração, mapeamento (use trechos de código para ilustrar a explicação).

  - Particionamento: É a decomposição do problema em pequenas tarefas [1].

É possível notar a etapa de particionamento no seguinte trecho de código:

```c
// A tarefa de executar um produto escalar é particionada em várias pequenas tarefas.
// Agora, para se executar um prod. escalar é preciso realizar várias
// tarefas que calculam a multiplicação entre os valores das matrizes e
// realizam as somas parciais desses valores.

void *dotprod_worker(void *arg)
{
   int i, k;
   long offset = (long) arg;
   double *a = dotdata.a;
   double *b = dotdata.b;     
   int wsize = dotdata.wsize;
   int start = offset*wsize;
   int end = start + wsize;
   double mysum;

   // Pequena tarefa executada em cada thread.
   for (k = 0; k < dotdata.repeat; k++) {
      mysum = 0.0;
      for (i = start; i < end ; i++)  {
        // Somas parciais realizada por cada tarefa.
         mysum += (a[i] * b[i]);
      }
   }

   pthread_mutex_lock (&mutexsum);
   dotdata.c += mysum;
   pthread_mutex_unlock (&mutexsum);

   pthread_exit((void*) 0);
}
```


  - Comunicação: É a determinação das estruturas e algoritmos necessários para a comunicação [1].

  ```c
  // Nesse trecho de código a estrutura para a comunicação entre as tarefas
  // é determinada. As threads irão se comunicar por meio de uma struct
  // que contêm a matriz A, a matriz B e o resultado do prod. escalar C. Ainda,
  // um mutex é iniciado, o mesmo define uma política de acesso a informação
  // entre as threads.
  typedef struct
   {
     double *a;
     double *b;
     double c;
     int wsize;
     int repeat;
   } dotdata_t;

  // Variaveis globais, acessiveis por todas threads
  dotdata_t dotdata;
  pthread_mutex_t mutexsum;
  ```
  ```c
  // Nesse trecho onde a fase da aglomeração é realizada, é possível perceber
  // a presença da comunicação entre as threads, pois o uso do mutex faz com que
  // as threads se comuniquem e sincronizem o acesso à variável C.
  // Linhas 45 - 47 do código.
  pthread_mutex_lock (&mutexsum);
  dotdata.c += mysum;
  pthread_mutex_unlock (&mutexsum);
  ```

  - Aglomeração: É a possível combinação de tarefas em tarefas maiores para o aumento de desempenho e diminuição de custos na comunicação [1].

  ```c
  // Aqui é possível perceber a fase de aglomeração, pois os resultados parciais
  // calculados por cada thread são somados à variável dotdata.c.

  // O cálculo da soma parcial é realizado:
  for (k = 0; k < dotdata.repeat; k++) {
     mysum = 0.0;
     for (i = start; i < end ; i++)  {
        mysum += (a[i] * b[i]);
     }
  }

  // E então "aglomerado" ao resultado final:
  pthread_mutex_lock (&mutexsum);
  dotdata.c += mysum;
  pthread_mutex_unlock (&mutexsum);
  ```

    - Mapeamento: É a distribuição de tarefas aos processadores.

    ```c
    // A função dotprod_threads (chamada pela main) define como as tarefas serão
    // distribuídas para cada thread.

    void dotprod_threads(int nthreads)
    {
       int i;
       pthread_t *threads;
       pthread_attr_t attr;

       threads = (pthread_t *) malloc(nthreads * sizeof(pthread_t));
       pthread_mutex_init(&mutexsum, NULL);

       pthread_attr_init(&attr);
       pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

       // Aqui, a tarefa é distribuída para nthreads. A tarefa a ser
       // realizada por cada thread é descrita pela função dotprod_worker().  
       for (i = 0; i < nthreads; i++) {
          pthread_create(&threads[i], &attr, dotprod_worker, (void *) i);
       }
       pthread_attr_destroy(&attr);
       for (i = 0; i < nthreads; i++) {
          pthread_join(threads[i], NULL);
       }
       free(threads);
    }
    ```
##### 2. Considerando o tempo (em microssegundos) mostrado na saída do programa, qual foi a aceleração (speedup) com o uso de threads?

 - Considerando a execução do cenário descrito abaixo, a aceleração encontrada foi de ~1.85.

 ```
  ./pthreads_dotprod 1 1000000 2000
  ./pthreads_dotprod 2 500000 2000
 ```


##### 3. A aceleração  se sustenta para outros tamanhos de vetores, números de threads e repetições? Para responder a essa questão, você terá que realizar diversas execuções, variando o tamanho do problema (tamanho dos vetores e número de repetições) e o número de threads (1, 2, 4, 8..., dependendo do número de núcleos). Cada caso deve ser executado várias vezes, para depois calcular-se um tempo de processamento médio para cada caso. Atenção aos fatores que podem interferir na confiabilidade da medição: uso compartilhado do computador, tempos muito pequenos, etc.

| Tamanho base do vetor  |  Mínimo Speedup |  Máximo Speedup |
|---|---|---|
| 1.000  | Speedup = 1.33. Cenário: 2 threads, Tam = 500, Rep = 1000 | Speedup = 1.97. Cenário: 4 threads, Tam = 250, Rep = 2500  |  
| 10.000 | Speedup = 1.56. Cenário: 2 threads, Tam = 5000, Rep = 500  | Speedup = 2.18. Cenário: 4 threads, Tam = 2500, Rep = 1500  |  
| 100.000  | Speedup = 1.71. Cenário: 2 threads, Tam = 50000, Rep = 1000  |  Speedup = 2.2. Cenário: 4 threads, Tam = 25000, Rep = 2000 |   
| 1.000.000  |  Speedup = 1.848. Cenário: 2 threads, Tam = 500000, Rep = 2000 | Speedup = 2.2116. Cenário: 4 threads, Tam = 250000, Rep = 2000  |   


##### 4. Elabore um gráfico/tabela de aceleração a partir dos dados obtidos no exercício anterior.

![1_mil](pthreads_dotprod/1_mil/graph.png)
![10_mil](pthreads_dotprod/10_mil/graph.png)
![100_mil](pthreads_dotprod/100_mil/graph.png)
![1_milhao](pthreads_dotprod/1_milhao/graph.png)

##### 5. Explique as diferenças entre [pthreads_dotprod.c](pthreads_dotprod/pthreads_dotprod.c) e [pthreads_dotprod2.c](pthreads_dotprod/pthreads_dotprod2.c). Com as linhas removidas, o programa está correto?

 - A diferença entre pthreads_dotprod.c e o pthreads_dotprod2.c está no uso do mutex na fase de aglomeração do resultado.




Referências:
- [1] Cláudio Geyer. Programação Paralela:Uma Introdução a MPI. ftp://ftp.inf.ufrgs.br/pub/geyer/PDP-CIC-ECP/slidesAlunos/SemestresAnteriores/ProvaP2-2017-1/pp03-tecnicas-MPI-Andre-v1d3-jun2017-gdocs.pdf.
- Autor. Título. Link.

------
## Parte II: OpenMP
