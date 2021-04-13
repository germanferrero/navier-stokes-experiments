# Haswell Buscando una metrica
En este experimento buscamos una validar que la métrica cantidad de celdas
procesadas por segundo en cada paso (`one_step`) es una métrica para comparar performance de [navier stokes](https://github.com/germanferrero/navier-stokes) que cumple con:
- Es comparable para cualquier tamaño del problema.
- Mejor performance para mayores valores.

## Como correrlo
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/celdas-por-segundo
make
```

## Desarrollo
Calculamos el valor de esta métrica para dos versiones del ejecutable headless:
- optimizado: compilado con -O3 -march=native
- no optimizado: compilado con -O0
Para cada uno de ellos hacemos corridas para varios tamaños de problema N.
Buscamos validar que:
- la métrica tiene valores similares para el mismo ejecutable para todos los valores de N.
- la métrica es más grande para la versión optimizada (que ya sabemos que es tiene menor wall-time)

Resultados:
|version| n| celdas_paso por segundo|
|-------|---|------------------------|
|optimizada| 32| 1263503.439515|
|no optimizada| 32| 836649.271261|
|optimizada| 64| 1151706.690607|
|no optimizada| 64| 837185.697323|
|optimizada| 128| 1108768.025772|
|no optimizada| 128| 827225.895941|
|optimizada| 256| 1069608.771422|
|no optimizada| 256| 735178.395689|

Vemos en el cuadro que cumple las dos propiedades que esperábamos.

## Conclusiones
- Celdas por segundo en cada paso: `N^2/(duracion de one_step)` es una métrica útil para comparar la performance de dos ejecutables en la misma arquitectura.