SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
SEQ_RESULTS_DIR=$(PWD)/seq_results
PARALLEL_RESULTS_DIR=$(PWD)/parallel_results
NS:=128 256 512 1024 2048 4096 8192 16384
MAX_THREADS:=20
VERSIONS:=navier-stokes-cuda
VERSIONS_PARALLELLS:=navier-stokes-lab3
all: $(PARALLEL_RESULTS_DIR)/stats.csv $(SEQ_RESULTS_DIR)/stats.csv

navier-stokes-lab3:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 9c0e4d8d498f0ccfe7e7a32cfe3dc3d483876d80 && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize -fopenmp" make headless

navier-stokes-cuda:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q d68554c6600b02c1b6276d2b33d4d42456620fbf && \
	make clean && make headless

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
