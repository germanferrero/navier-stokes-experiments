import glob
import csv
import re
import os
import sys
import fileinput

def parse_stats(stats):
    uops_executed_port_0 = int(stats[0][0])
    uops_executed_port_1 = int(stats[1][0])
    nanoseconds = int(stats[0][3])
    flop = uops_executed_port_0 + uops_executed_port_1
    gflops = float(flop) / nanoseconds
    gflop = flop / 1.0e9
    return gflop, gflops, nanoseconds / 1.0e9

def main():
    stats = []
    for line in fileinput.input():
        stats.append(line.strip().split(','))
    gflop, gflops, seconds = parse_stats(stats)
    print('GFLOP,GFLOPS,Time(sec)')
    print(','.join([
        '{:.2f}'.format(gflop),
        '{:.2f}'.format(gflops),
        '{:.2f}'.format(seconds)
    ]))

if __name__ == '__main__':
    main()
