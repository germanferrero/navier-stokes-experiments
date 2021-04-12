# Haswell Comparando GFLOPS entre Compiladores
En este experimento comparamos la performance de GCC y Clang (en distintas versionas) para distintos tamaños de N con -O3 y -march=haswell.

## Como correrlo
```
git clone git@github.com:germanferrero/navier-stokes-experiments.git
cd navier-stokes-experiments/haswell-gflops-compilers
sudo ansible-playbook -i ./inventory dependencias.yml
make
```

## En que consiste

Corremos ./headless para distintos tamaños de N: 64, 128, 256 midiendo GFLOPS. Lo hacemos para ambos compiladores, gcc y clang usando solo el flag de -O3. El resultado se guarda en una tabla.
Para GFLOPS, en la arquitectura Haswell utilizamos:
`GLOPS= (µops ejecutadas en puerto 0 y puerto 1) / segundos`
Más info de la obtención de esta métrica en [haswell-looking-for-a-metric](../haswell-looking-for-a-metric)

### TODO
Plotear la métrica en un gráfico de líneas
