import re
import os
import sys
import fileinput
import csv
import matplotlib.pyplot as plt
from contextlib import contextmanager
from itertools import groupby
from collections import namedtuple

Stat = namedtuple('stat', ['compiler', 'n', 'cells_p_s'])

def read_stats(path):
    with open(path) as ifile:
        reader = csv.DictReader(ifile, fieldnames=Stat._fields)
        next(reader) # skip header
        for row in reader:
            row['n'] = int(row['n'])
            row['cells_p_s'] = float(row['cells_p_s'])
            stat = Stat(**row)
            yield stat
            

def main():
    stats = read_stats(sys.argv[1])
    stats_sorted = sorted(stats, key=lambda s: s.compiler)
    stats_groupped = groupby(stats_sorted, key=lambda s: s.compiler)

    fig, ax = plt.subplots()
    ns = set()
    for ix, (compiler, compiler_stats) in enumerate(stats_groupped):
        xs = []
        ys = []
        for s in compiler_stats:
            xs.append(s.n)
            ys.append(s.cells_p_s)
            ns.add(s.n)
        ax.plot(xs, ys, color='C{}'.format(ix), label=compiler)
    ax.grid()
    ax.legend(loc="lower left")
    ax.set_xticks(list(ns))
    ax.set_xlabel('N')
    ax.set_ylabel('Celdas/s (1e6)')
    ax.set_title('Comparación de Celdas/s entre compiladores')
    fig.savefig(sys.argv[2])

if __name__ == '__main__':
    main()
