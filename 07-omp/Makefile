SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
SEQ_RESULTS_DIR=$(PWD)/seq_results
PARALLEL_RESULTS_DIR=$(PWD)/parallel_results
NS:=128 256 512 1024 2048 4096 8192
MAX_THREADS:=20
VERSIONS:=lab2 redblack-vec
VERSIONS_PARALLELLS:=redblack-omp-only-linsolve
all: $(PARALLEL_RESULTS_DIR)/stats.csv

navier-stokes-lab2:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q d4e200efcdc6e900057a348753f145e4553fd454 && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-redblack-vec:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q a2d230bd724764f20a08903a20f89a980e99af0f && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize" make headless

navier-stokes-redblack-omp-only-linsolve:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 4e3f64287d69ea9c8131a7c5c0ea8d0bfa3d54c6 && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize -fopenmp" make headless


navier-stokes-redblack-omp:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 8383fe0d95093e4a736991e014921b95338de9f2 && \
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
