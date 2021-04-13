SHELL:=/bin/bash
PERF_CODES=-e r5301a1 -e r5302a1
RESULTS_DIR=$(PWD)/results
CC:=gcc-7
all: $(RESULTS_DIR)/runs-finish-mark $(RESULTS_DIR)/optimized_avx_vmulls.txt $(RESULTS_DIR)/not_optimized_avx_vmulls.txt

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

$(RESULTS_DIR)/optimized_avx_vmulls.txt: navier-stokes-optimized
	cd $< && $(CC) -std=c11 -Wall -Wextra -Wno-unused-parameter -O3 -march=haswell solver.c -S &&\
	grep vmulss solver.s | wc -l > $@

$(RESULTS_DIR)/not_optimized_avx_vmulls.txt: navier-stokes-not-optimized
	cd $< && $(CC) -std=c11 -Wall -Wextra -Wno-unused-parameter -O0 solver.c -S && \
	grep vmulss solver.s | wc -l > $@

$(RESULTS_DIR)/runs-finish-mark: navier-stokes-not-optimized navier-stokes-optimized
	PERF_CODES="$(PERF_CODES)" \
	RESULTS_DIR=$(RESULTS_DIR) \
	./runs.sh && touch $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all