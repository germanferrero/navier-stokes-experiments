PERF_CODES=-e r5301a1 -e r5302a1

all: gflops_n_32.txt gflops_n_64.txt gflops_n_128.txt gflops_n_256.txt

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q d83b5a24d9f3d9c50ab91dae32621cc948aebeb2 && \
	make clean && CEXTRAFLAGS="-O2" make

gflops_n_%.txt: navier-stokes
	perf stat -x ',' $(PERF_CODES) ./navier-stokes/headless $* 0.1 0.0 0.0 5.0 100.0 2>&1 1>/dev/null \
	| python get_gflops.py > $@

clean:
	rm -rf navier-stokes gflops_n_*.txt

.PHONY = clean all