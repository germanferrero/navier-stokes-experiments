#! /bin/bash
set -e
mkdir -p $RESULTS_DIR
cd navier-stokes-optimized
perf stat -x ',' $PERF_CODES ./headless 128 0.1 0.0 0.0 5.0 100.0 2>&1 1>/dev/null \
| python ../parse_stats.py > $RESULTS_DIR/optimized_stats.csv
cd ..
cd navier-stokes-not-optimized
perf stat -x ',' $PERF_CODES ./headless 128 0.1 0.0 0.0 5.0 100.0 2>&1 1>/dev/null \
| python ../parse_stats.py > $RESULTS_DIR/not_optimized_stats.csv
cd ..