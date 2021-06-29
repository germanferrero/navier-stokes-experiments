# Haswell Comparando GFLOPS entre Compiladores
En este experimento comparamos la performance de gcc[-08 -09 -10] y clang[-10 -11 -12] para distintos tamaños de N con -O3 y -march=native.

## Como correrlo
Primero instalar los requisitos listados en el [README]('../README.md')
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/04-compilers-comparison
make
```

## En que consiste

Corremos ./headless para distintos tamaños de N: 64, 128, 256, 512 midiendo celdas por segundo en cada paso. Lo hacemos para todos los compiladores usando solo el flag de -O3 y -march=native. El resultado se guarda en una tabla, y esa tabla luego la graficamos con un gráfico de lineas.
La métrica utilizada es celdas por segundo en cada paso.
Más info de esta métrica en [haswell-looking-for-a-metric](../02-haswell-looking-for-a-metric)

# Conclusiones

No vimos diferencia notable entre compiladores. Elegimos clang-12 para el resto de los laboratorios de manera arbitraria.