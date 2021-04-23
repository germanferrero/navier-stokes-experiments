SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
RESULTS_DIR=$(PWD)/results
NS:=64 128 256 512 1024 2048 4096 8192
VERSIONS:= baseline fix-index independent-uops-first
all: $(RESULTS_DIR)/stats.png

navier-stokes-baseline:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 440805de249b86ea4c6e2c47ebd8306e5b2437d7 && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-fix-index:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 53bc5181773bec55d9dfa89d001ecf38c6e844b8 && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-independent-uops-first:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q eff8c44374d35b9f1dca6d4be77d10e97275cd4d && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

navier-stokes-just-distribute:
	git clone https://github.com/germanferrero/navier-stokes.git $@ && \
	cd $@ && git checkout -q 1111cd78a89b6db305c7048c4f85c9468b6c0b4d && \
	make clean && CEXTRAFLAGS="-O3 -march=native -ffast-math" make headless

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
