SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
RESULTS_DIR=$(PWD)/results
NS:=32 64 128 180 256 400 512 1024 2048 4096 8192
VERSIONS:=independent-uops-first diagonals
all: $(RESULTS_DIR)/stats.png

navier-stokes-independent-uops-first:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q eff8c44374d35b9f1dca6d4be77d10e97275cd4d && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-diagonals:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 00e49e3321bef84efe28347dc0ee27dbf1458821 && \
	make clean && CEXTRAFLAGS="-O1 -march=native -ffast-math -ftree-vectorize" make headless

$(RESULTS_DIR)/stats.csv: $(foreach version,$(VERSIONS), navier-stokes-$(version))
	VERSIONS="$(VERSIONS)" \
	NS="$(NS)" \
	RESULTS_DIR=$(RESULTS_DIR) \
	./runs.sh

$(RESULTS_DIR)/stats.png: $(RESULTS_DIR)/stats.csv
	python plot_stats.py $< $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all
