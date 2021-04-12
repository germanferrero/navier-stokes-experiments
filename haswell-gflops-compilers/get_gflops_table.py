import glob
import csv
import re
import os

def get_gflops(stats):
    uops_executed_port_0 = int(stats[0][0])
    uops_executed_port_1 = int(stats[1][0])
    nanoseconds = int(stats[0][3])
    gflops = float(uops_executed_port_0 + uops_executed_port_1) / nanoseconds
    return gflops

def main():
    filenames = glob.glob('results/perf_stats_*.csv')
    for fname in filenames:
        with open(fname) as ofile:
            stats = list(csv.reader(ofile))
            match = re.match(r'perf_stats_(.*?)_(\d+).csv', os.path.basename(fname))
            compiler, n = match.groups()
            gflops = get_gflops(stats)
            print(','.join([compiler, n, '{:.2f}'.format(gflops)]))

if __name__ == '__main__':
    main()