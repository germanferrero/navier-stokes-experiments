SHELL:=/bin/bash
PERF_CODES=-e r5301a1 -e r5302a1
RESULTS_DIR=$(PWD)/results
CC:=gcc-7
all: $(RESULTS_DIR)/runs-finish-mark

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q d83b5a24d9f3d9c50ab91dae32621cc948aebeb2 && \
	cd ..

navier-stokes-optimized: navier-stokes
	cp -r navier-stokes $@ && cd $@ && \
	make clean && CC=$(CC) CEXTRAFLAGS="-O3 -march=haswell" make headless

navier-stokes-not-optimized: navier-stokes
	cp -r navier-stokes $@ && cd $@ && \
	make clean && CC=$(CC) CEXTRAFLAGS="-O0" make headless

$(RESULTS_DIR)/runs-finish-mark: navier-stokes-not-optimized navier-stokes-optimized
	PERF_CODES="$(PERF_CODES)" \
	RESULTS_DIR=$(RESULTS_DIR) \
	./runs.sh && touch $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all