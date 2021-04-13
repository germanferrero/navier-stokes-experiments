SHELL:=/bin/bash
PERF_CODES=-e r5301a1 -e r5302a1
UBUNTU_RELEASE=$(lsb_release -cs)
RESULTS_DIR=$(PWD)/results
NS:=32 64
COMPILERS:=gcc-8 gcc-9 gcc-10 clang-10 clang-11 clang-12
all: $(RESULTS_DIR)/gflops.csv

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q d83b5a24d9f3d9c50ab91dae32621cc948aebeb2 && \
	cd ..

navier-stokes-%: navier-stokes
	cp -r navier-stokes navier-stokes-$* && cd $@ && \
	make clean && CC="$*" CEXTRAFLAGS="-O3 -march=haswell" make headless

$(RESULTS_DIR)/runs-finish-mark: $(foreach compiler,$(COMPILERS), navier-stokes-$(compiler))
	COMPILERS="$(COMPILERS)" \
	NS="$(NS)" \
	PERF_CODES="$(PERF_CODES)" \
	RESULTS_DIR=$(RESULTS_DIR) \
	./runs.sh && touch $@

$(RESULTS_DIR)/gflops.csv: $(RESULTS_DIR)/runs-finish-mark
	python get_gflops_table.py > $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all gcc clang