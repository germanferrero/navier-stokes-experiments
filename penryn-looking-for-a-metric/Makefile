PERF_CODES=-e r530210


all: stats_n_32.txt stats_n_64.txt stats_n_128.txt stats_n_256.txt

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q d83b5a24d9f3d9c50ab91dae32621cc948aebeb2 && \
	make clean && CEXTRAFLAGS="-O2 -O3" make

stats_n_%.txt: navier-stokes
	perf stat -d -d $(PERF_CODES) -o $@ ./navier-stokes/headless $* 0.1 0.0 0.0 5.0 100.0

clean:
	rm -rf navier-stokes stats_n_*.txt

.PHONY = clean all
