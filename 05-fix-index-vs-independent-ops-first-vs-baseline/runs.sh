#! /bin/bash
set -e
mkdir -p $RESULTS_DIR
echo "version, n, celdas/s en c/paso" > ${RESULTS_DIR}/stats.csv
for n in $NS; do
    for version in $VERSIONS; do
        cd navier-stokes-$version
        cell_step_per_s=$(./headless $n 0.1 0.0 0.0 5.0 100.0 2>/dev/null)
        echo "$version,$n,$cell_step_per_s" >> ${RESULTS_DIR}/stats.csv
        cd ..
    done
done