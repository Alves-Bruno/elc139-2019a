**Nome:** Bruno da Silva Alves.

**Disciplina:** elc139-2019a (Programação Paralela).

**Descrição do Hardware:**

Dell Inspiron 15R (7520)
2 Cores com 2 threads por cores
Intel(R) Core(TM) i5-3230M (Intel Core IvyBridge processor)
Freq. Proc. = ~3.00GHz
Memória = 7852.04 MB (Cache L1: 2x 32kB, Cache L2: 2x 256kB, Cache L3: 1x 3MB)
Ubuntu 18.04.1 LTS

-----------------------------

## Parte 1:

**Código:** [matrix_modified](matrix_mult_sr_modified.c).

As modificações foram comentadas no código.

--------------

## Parte 2:

Resumo crítico do artigo "Send-receive considered harmful: Myths and realities of message passing":

**INTRODUÇÃO:**

O desenvolvimento de programas para sistemas paralelos e distribuídos continua sendo uma tarefa difícil. O uso de send e recv resulta em processos de programação complicados. O uso de send e recv pode ser considerado tão perigoso quanto o uso de goto.

Os autores avaliaram o uso de operações coletivas em relação ao uso de send e receive sobre os seguintes aspectos:

* Simplicidade
* Programabilidade
* Expressividade
* Performance
* Preditibilidade

**SIMPLICIDADE:**

Os autores ressaltam que as operações coletivas descrevem como os dados são distribuídos entre a fase de comunicação e de processamento, já com o uso de send e recv, essa divisão não é tão clara.

O uso de send e recv torna o programa mais difícil de ser entendido e corrigido. As 16 variações de send e recv tornam o código menos compreensível e difícil escolher qual se encaixa melhor em cada caso, ainda que essa técinica permita mais flexibilidade em relação ao uso de operações coletivas.

Com o uso que tive dessas duas estratégias, percebi que o uso das operações coletivas de fato tornaram o entendimento do código mais simplificado. Ao ler os códigos que utilizam send e recv, é necessário interpretar cada operação de forma mais avançada para realmente compreender o que está acontecendo no sistema.

**PROGRAMABILIDADE:**

No artigo o exemplo do MPI_reduce é utilizado para provar que operações coletivas facilitam transformações de alto nível que podem ser aplicadas no processo de construção de programas. Ou seja, o uso de operações coletivas facilita o trabalho de estimativa de complexidade dos algoritmos.

**EXPRESSIVIDADE:**

Os autores mostram algumas aplicações importantes que utilizaram somente operações coletivas que executaram sem perdas de performance significativas. As operações coletivas cobrem grande parte dos padrões de comunicações utilizados em aplicações paralelas importantes.

No uso restrito que tive, não experimentei dificuldades para expressar algoritmos utilizando as operações coletivas.

**PERFORMANCE:**

É demonstrado que o pensamento de que "programas utilizam send e recv são naturalmente mais rápidos que programas que utilizam operações coletivas" não é verdade, pois:

1. A implementação das operações coletivas são implementadas por pessoas que estão bem mais familiarizados com aplicações paralelas. Aplicações que utilizam send e recv podem não ser aplicáveis a ambientes diferentes do qual foram testadas.

2. Na maioria das vezes, operações coletivas são implementadas com a ajuda do hardware e não somente com send e recv, assim aumentando a performance.

Portanto, existem fortes evidências de que a utilização de send e recv não oferecem vantagens em termos de performance.

**PREDITIBILIDADE:**

Os autores provam que a utilização das operações coletivas contribuem para o desafio de previsão das características do programa sem executá-lo. Mesmo sem realizar uma análise profunda sobre os códigos que desenvolvi, percebi que o uso de operações coletivas contribuíram para o meu entendimento prévio do que aconteceria no programa, antes mesmo de executá-lo.


---------------
