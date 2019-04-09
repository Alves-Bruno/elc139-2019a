**Nome:** Bruno da Silva Alves.

**Disciplina:** elc139-2019a (Programação Paralela).

**Programa desenvolvido:** [OpenMPDemoABC](OpenMPDemoABC.cpp).

**Referência:** https://computing.llnl.gov/tutorials/openMP/#Introduction

-------------------
### Exemplo de saída do programa, com explicação dos casos de teste:

#### 1. Schedule `static`, com e sem especificação do `chunk`

**#pragma omp parallel for schedule (static)**
```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```

**#pragma omp parallel for schedule (static, chunk)**

```
chunk = 20
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```
```
chunk = 40
Case : using OpenMP (expecting correct results)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=40 B=20 C=0
```

```
chunk = 60
Case : using OpenMP (expecting correct results)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
A=60 B=0 C=0
```


> As iterações do loop são divididas em pedaços do tamanho de chunk e são estaticamente atribuídas as threads. Foi possível perceber que a execução sem o chunk divide as iterações igualmente entre o número de threads disponíveis. O caso em que o chunk = 20 é especificado é similar a executar sem a determinação do chunk.


----------------

#### 2. Schedule `dynamic`, com e sem especificação do `chunk`

**#pragma omp parallel for schedule (dynamic)**
```
Case : using OpenMP (expecting correct results)
BCBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAC
A=1 B=57 C=2
```

```
Case : using OpenMP (expecting correct results)
BCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAB
A=1 B=2 C=57
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCBA
A=2 B=1 C=57
```

**#pragma omp parallel for schedule (dynamic, chunk)**
```
chunk = 20
Case : using OpenMP (expecting correct results)
CAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
chunk = 20
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
chunk = 20
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
chunk = 40
Case : using OpenMP (expecting correct results)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=40 B=20 C=0
```

```
chunk = 60
Case : using OpenMP (expecting correct results)
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
A=0 B=0 C=60
```

> As iterações do loop são divididas em pedaços do tamanho de chunk e são dinamicamente atribuídas as threads. Quando não especificado, o chunk é igual a 1. Quando o chunk não foi especificado, percebeu-se que as execuções foram predominantes em uma thread. Quando o chunk = 20, as saídas foram similares a execução com a cláusula STATIC.

--------------

#### 3. Schedule `guided`, com e sem especificação do `chunk`

**#pragma omp parallel for schedule (guided)**
```
Case : using OpenMP (expecting correct results)
ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCAAAAAAAAAAAAAAAAAAA
A=20 B=31 C=9
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBB
A=20 B=14 C=26
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBB
A=20 B=14 C=26
```

**#pragma omp parallel for schedule (guided, chunk)**
```
chunk = 20
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
chunk = 20
Case : using OpenMP (expecting correct results)
BCCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```

```
chunk = 20
Case : using OpenMP (expecting correct results)
ABACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

```
chunk = 40
Case : using OpenMP (expecting correct results)
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAA
A=20 B=40 C=0
```

```
chunk = 60
Case : using OpenMP (expecting correct results)
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
A=0 B=60 C=0
```

> As iterações são dinamicamente atribuídas as threads em blocos, enquanto houverem blocos para serem distribuídos. O tamanho do bloco diminui a cada vez que o mesmo é atribuído a uma thread. O bloco inicial é calculado da seguinte forma: iterações / threads . Quando o chunk é especificado, é possível perceber que a execução ocorre de forma similar a cláusula DYNAMIC. Quando o chunk não é especificado, o número de escritas de cada tipo é dependente de quantas vezes um bloco foi atribuído para alguma thread.

-----------------------

#### 4. Schedule `runtime`

**#pragma omp parallel for schedule (runtime)**

```
Case : using OpenMP (expecting correct results)
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
A=0 B=60 C=0
```

```
Case : using OpenMP (expecting correct results)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
A=60 B=0 C=0
```

```
Case : using OpenMP (expecting correct results)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
A=60 B=0 C=0
```

> A decisão de escalonamento é adiada até que o programa seja executado. Não especifiquei nenhum parâmetro para a variável de ambiente OMP_SCHEDULE. O programa executou o loop de forma serial em das threads disponíveis.
------------------------

#### 5. Schedule `auto`

**#pragma omp parallel for schedule (auto)**

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```

```
Case : using OpenMP (expecting correct results)
ACBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAA
A=20 B=20 C=20
```

```
Case : using OpenMP (expecting correct results)
ACCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
A=20 B=20 C=20
```

> O escalonamento é delegado para o compilador ou a variável de ambiente de escalonamento. Em comparação com as outras saídas, é possível inferir que o compilador utilizou a cláusula STATIC com chunk igual a 20.

------------------

####  6. Um ou mais casos sem exclusão mútua, para apresentar saídas incorretas.


```
STATIC:
Case : using OpenMP (expecting incorrect results)
CBACBACBCABABACBACBACBACBACBACBABCABCABCABCABCABABCABCA-C-CC
A=19 B=19 C=20
```

```
DYNAMIC:
Case : using OpenMP (expecting incorrect results)
CBACBACACBCABCABCBCBACBACBACACABCABCBCABCABCABCABCABCABCAB--
A=18 B=19 C=21
```

```
AUTO:
Case : using OpenMP (expecting incorrect results)
CABBACBCBCABCBACABCBACBCBCABCABCABCABCABCABCBACBACBAC-ACA-AA
A=19 B=19 C=20
```
