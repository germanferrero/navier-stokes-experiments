#! /bin/bash
set -e
mkdir -p $RESULTS_DIR
echo "version, n, threads, celdas/s en c/paso" > ${RESULTS_DIR}/stats.csv
for n in $NS; do
    for version in $VERSIONS; do
        cd navier-stokes-$version
        for num_threads in $(seq 1 $MAX_THREADS); do
            cell_step_per_s=$(OMP_NUM_THREADS=$num_threads srun ./headless $n 0.1 0.0 0.0 5.0 100.0 2>/dev/null)
            echo "$version,$n,$num_threads,$cell_step_per_s" >> ${RESULTS_DIR}/stats.csv
        done
        cd ..
    done
done
