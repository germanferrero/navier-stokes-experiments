# Penryn  Buscando una metrica
En este experimento buscamos una métrica útil para denotar la performance de [navier stokes](https://github.com/germanferrero/navier-stokes).

## Como correrlo
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/haswell-looking-for-a-metric
make
```

## En que consiste

Usamos `perf stat` sobre una arquitectura penryn
con `perf stat -d -d` obtenemos métricas standar de performance,
y con `perf stat -e r<codigo>` obtenemeos métricas específicas del PMU de Penryn
| Codigo | Descripción |
|--------|-------------|
| 531010 | µops ejecutadas en el puerto 0 de Haswell. Que incluye: FP FMA, FP MUL, FP DIV |
|        | µops ejecutadas en el puerto 1 de Haswell. Que incluye: FP FMA, FP MUL, FP ADD | 
|        | µops ejecutadas en el puerto 2 de Haswell. Que incluye: load data | 
|        | µops ejecutadas en el puerto 3 de Haswell. Que incluye: load data | 
|        | µops ejecutadas en el puerto 4 de Haswell. Que incluye: store data |

Estos códigos fueron obtenidos siguiendo la [guía](https://cs.famaf.unc.edu.ar/~nicolasw/Docencia/CP/2021/instructivo_flops.html) los compañeros de la materia Bordon, Mauro y Garagiola, Nazareno

## Que resultados se obtuvieron
TODO
