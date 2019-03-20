[Programação Paralela](https://github.com/AndreaInfUFSM/elc139-2018a) > T1

TOP500 & me: Comparativo de Arquiteturas Paralelas
--------------------------------------------------

Nome: Bruno da Silva Alves

| Característica                                            | Computador no TOP500  | Meu computador  |
| --------------------------------------------------------- | --------------------- | --------------- |
| Nome/Título                                               | Summit - IBM Power System AC922, IBM POWER9(Ranking top500 - 001)                      |       Dell Inspiron 15R (7520)          |
| Imagem (foto, diagrama, screenshot, etc.)                 | <img src="https://www.datacenterknowledge.com/sites/datacenterknowledge.com/files/styles/gal_landscape_main_2_retina/public/summit%20supercomputer%20ornl%20ibm_2.jpg?itok=ZYeTSzga">| <img src="https://laptopmedia.com/wp-content/uploads/2014/12/5724__3-e1422093307195.jpg"> |
| Classificação de Flynn                                    |         MIMD              |        MISD         |
| Memória: compartilhada, distribuída ou ambas?             |           Ambas            |       Compartilhada          |
| Número total de núcleos de processamento                  |       2.397.824 núcleos. Cada processador possui 24 núcleos, cada núcleo suporta até 4 threads. Cada computador (AC922 server) pode possuir 2 processadores (2 sockets).         | 2 Cores com 2 threads por cores.              |
| Fabricante e modelo do(s) processador(es)                 |       IBM - IBM POWER9 22C 3.07GHz               |       Intel(R) Core(TM) i5-3230M  (Intel Core IvyBridge processor)          |
| Frequência do(s) processador(es)                          |  Segundo top500, 3.07GHz. Mas suporta dois tipos de configurações: 18-core 3.15 GHz (3.45 GHz turbo) processor module ou 22-core 2.80 GHz (3.10 GHz turbo) processor module.                     |        Frequências disponíveis: 1.2GHz - 3.2GHz. Em modo powersave min = 1.184, atual = 1.371, max = 3.2 GHz. Em modo performance min = 1.184, atual = 3.004, max = 3.2        |
| Memória total                                             |    	2,801,664 GB                    |        Total memory:		7852.04 MB (Cache L1: 2x 32kB, Cache L2: 2x 256kB, Cache L3: 1x 3MB)         |
| Tipo(s) de interconexão entre os núcleos/processadores    | 	Dual-rail Mellanox EDR Infiniband |      ***           |
| Desempenho Linpack                                      |        143,500 TFlop/s               |         HPLinpack 2.1, HP Linpack benchmark, October 26, 2012: 25.2547 Gflops/s|

### Referências
- Data Center Knowledge. The World’s 10 Fastest Supercomputers – in Pictures. https://www.datacenterknowledge.com/supercomputers/world-s-10-fastest-supercomputers-pictures/gallery?slide=1.
- Laptopmedia. Dell Inspiron 15R (7520). https://laptopmedia.com/laptop-specs/dell-inspiron-15r-7520/.
- Alexandre Bicas Caldeira (IBM). IBM Power System AC922 Introduction and Technical Overview. https://www.redbooks.ibm.com/redpapers/pdfs/redp5472.pdf.
- Medições locais feitas com a ferramenta likwid. https://github.com/RRZE-HPC/likwid.
