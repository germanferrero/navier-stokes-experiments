import glob
import csv
import re
import os
import sys
import fileinput

def get_gflops(stats):
    uops_executed_port_0 = int(stats[0][0])
    uops_executed_port_1 = int(stats[1][0])
    nanoseconds = int(stats[0][3])
    flop = uops_executed_port_0 + uops_executed_port_1
    gflops = float(flop) / nanoseconds
    gflop = flop / 1.0e9
    return gflop, gflops

def main():
    stats = []
    for line in fileinput.input():
        stats.append(line.strip().split(','))
    gflop, gflops = get_gflops(stats)
    print('{:.2f}'.format(gflop), '{:.2f}'.format(gflops))

if __name__ == '__main__':
    main()
