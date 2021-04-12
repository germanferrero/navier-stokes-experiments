#! /bin/bash
set -e
mkdir -p $RESULTS_DIR
echo $COMPILERS
echo $NS
for compiler in $COMPILERS; do
    for n in $NS; do
        cd navier-stokes-$compiler
        perf stat -x ',' $PERF_CODES \
        ./headless $n 0.1 0.0 0.0 5.0 100.0 2>$RESULTS_DIR/perf_stats_${compiler}_${n}.csv
        cd ..
    done
done