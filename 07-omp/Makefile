SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
SEQ_RESULTS_DIR=$(PWD)/seq_results
PARALLEL_RESULTS_DIR=$(PWD)/parallel_results
NS:=128 256 512 1024 2048 4096 8192
MAX_THREADS:=20
VERSIONS:=lab2 redblack-vec
VERSIONS_PARALLELLS:=redblack-omp
all: $(PARALLEL_RESULTS_DIR)/stats.csv $(SEQ_RESULTS_DIR)/stats.csv

navier-stokes-lab2:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 1f9d4c8c87def959d6cf80d6a21e5f154529c2dd && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-redblack-vec:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q e8b8772440a13dba8fc6f2af8105b27a163fcf52 && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize" make headless

navier-stokes-redblack-omp:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 9c0e4d8d498f0ccfe7e7a32cfe3dc3d483876d80 && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize -fopenmp" make headless

$(SEQ_RESULTS_DIR)/stats.csv: $(foreach version,$(VERSIONS), navier-stokes-$(version))
	VERSIONS="$(VERSIONS)" \
	NS="$(NS)" \
	RESULTS_DIR=$(SEQ_RESULTS_DIR) \
	./run_seq.sh

$(PARALLEL_RESULTS_DIR)/stats.csv: $(foreach version,$(VERSIONS_PARALLELLS), navier-stokes-$(version))
	VERSIONS="$(VERSIONS_PARALLELLS)" \
	NS="$(NS)" \
	RESULTS_DIR=$(PARALLEL_RESULTS_DIR) \
	MAX_THREADS=$(MAX_THREADS) \
	./run_parallel.sh

# $(RESULTS_DIR)/stats.png: $(RESULTS_DIR)/stats.csv
# 	python plot_stats.py $< $@

clean:
	rm -rf $(SEQ_RESULTS_DIR) $(PARALLEL_RESULTS_DIR) navier-stokes*

.PHONY = clean all
