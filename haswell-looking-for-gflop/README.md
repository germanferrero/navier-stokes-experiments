# Haswell Buscando una metrica
En este experimento buscamos una forma de calcular GFLOP (Giga operaciones de punto flotante) en la arquitectura de haswell.

## Como correrlo
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/haswell-looking-for-gflop
make
```

## Desarrollo

Usamos `perf stat` sobre una arquitectura Haswell.
y con `perf stat -e r<codigo>` obtenemeos métricas específicas del PMU de Haswell.

En la arquitectura de Haswell no hay ningún evento que denote la ejecución de operaciones de punto flotante en si. Pero si hay eventos que denotan la ejecución de operaciones en cada puerto de esta arquitectura.
Podemos ver qué unidades de ejecución se encuentran en cada puerto de esta arquitectura en la [wikichip](https://en.wikichip.org/wiki/File:haswell_block_diagram.svg).
De allí elegimos el puerto 0 y el puerto 1 como los puertos que concentran las operaciones de punto flotante. Estos son sus códigos para pasarle a perf.

| Codigo | Descripción |
|--------|-------------|
| 5301a1 | µops ejecutadas en el puerto 0 de Haswell. Que incluye: FP FMA, FP MUL, FP DIV |
| 5302a1 | µops ejecutadas en el puerto 1 de Haswell. Que incluye: FP FMA, FP MUL, FP ADD | 

> Estos códigos fueron obtenidos siguiendo la [guía](https://cs.famaf.unc.edu.ar/~nicolasw/Docencia/CP/2021/instructivo_flops.html) los compañeros de la materia Bordon, Mauro y Garagiola, Nazareno

Utilizamos entonces:
`GFLOPS = (µops ejecutadas en puerto 0 y puerto 1) / segundos`

Que es, aunque esos puertos contienen otras unidades de ejecución además de las de punto flotante, una aproximación suficientemente buena de la cantidad de operaciones de punto flotante en Haswell (al menos sumas, multiplicaciones y divisiones).

Calcular FLOPS de manera precisa es algo [difícil de lograr](https://linux-perf-users.vger.kernel.narkive.com/s7GIb114/some-troubles-with-perf-and-measuring-flops)

Ponemos a prueba esa métrica para ver que cumpla con lo siguiente:
- Incrementa en el órden de N^2 para distintos tamaños N de problema. Es decir si el tamaño del problema se duplica los GFLOP se cuadriplican.
 - Como consecuencia, puesto que el tiempo de ejecución también se cuadriplica, los GFLOPS se mantienen constantes para distintos tamaños de problema.

*Resultados*

|n | GFLOP | GFLOPS|
|--|-------|-------|
|32 | 1.75 | 0.99|
|64 | 7.07 | 0.91|
|128 | 28.29 | 0.85|
|256 | 114.17 | 0.81|

## Conclusiones
- Aunque calcular GFLOPS de manera precisa no es fácil de lograr, y menos en Haswell. Tomamos:
`GFLOPS = (µops ejecutadas en puerto 0 y puerto 1) / segundos`
como una aproximación válida.
- Cumple con la propiedades deseadas:
 - si el tamaño del problema se duplica los GFLOP se cuadriplican.
 - los GFLOPS se mantienen constantes para distintos tamaños de problema.
