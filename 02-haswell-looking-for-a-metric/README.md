# Haswell Buscando una metrica
En este experimento buscamos una métrica útil para denotar la performance de [navier stokes](https://github.com/germanferrero/navier-stokes).

## Como correrlo
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/haswell-looking-for-a-metric
make
```

## Desarrollo
### Sirve GFLOPS?
Si utilizamos gflops como métrica de perfomance. Podemos penalizar más a un programa que tenga menos operaciones por segundo, pero dure menos tiempo de pared por que resuelve el problema en menos operaciones.

Hipotesis H0: Dado un tamaño de problema N, la cantidad de operaciones punto flotante para resolver headless es fija.

De ser verdadera, es justo comparar la performance mediante GFLOPS, ya que
mayor GFLOPS implica menor wall time.
De ser falsa, es injusto comparar la performance mediante GFLOPS, ya que
mayor GFLOPS no implica menor wall time.

Como contra ejemplo a la hipótesis, probamos ejecutando headless para N=128, con -O3 -march=haswell vs -O0. Obteniendo los siguientes resultados:

|Compilación|GFLOP|GFLOPS|Time(Sec)|
|-----------|-----|------|---------|
|-O0|90.32|2.21|40.82|
|-O3 -march=haswell|26.22|0.88|29.80|

HO es Falsa, la versión optimizada hace tres veces menos GFLOP que la no optimizada.
Además resulta que la optimizada tarda 11 segundos menos.

Entonces GFLOPS no sirve para comparar 2 soluciones entre sí. Pero puede darnos una idea de cuánto se está exprimiendo el CPU, en comparación a por ejemplo el Empirical Roofline Toolkit.

#### Por qué la versión optimizada hace menos GFLOP?
La hipótesis que queda a validar es que se hacen menos GFLOP por que el compilador está vectorizando las operaciones de punto flotante.
Con lo cuál realiza menos GFLOP en total.

|Compilación|Cantidad de operacions vmulss (AVX) en el assembly|
|-----------|-----------------------------------|
|-O0|0|
|-O3 -march=haswell| 131|


### Celdas por segundo
La cantidad de celdas de la matriz procesadas por segundo debería ser una métrica que cumple:
 - Comparable para cualquier tamaño del problema.
 - Mejor performance para mayores valores.

## FAQ
### Cómo calculamos GFLOP?
`GFLOPS = (µops ejecutadas en puerto 0 y puerto 1) / segundos`
Más detalle en ['haswell-looking-for-gflop']('../haswell-looking-for-gflop')

## Conclusiones
- GFLOPS no es fiable para comparar la performance de dos ejecutables ya que: dado un tamaño de problema N, la cantidad de operaciones punto flotante para resolver headless *no* es fija.
- GFLOPS puede servir para saber cuánto margen tenemos para optimizar el uso del CPU, en comparación con un test como Empirical Roofline Toolkit.
- Celdas por segundo: `N^2/segundos` debería ser una métrica útil para comparar la performance de dos ejecutables en la misma arquitectura. A validar.