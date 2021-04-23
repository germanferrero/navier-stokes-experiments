SHELL:=/bin/bash
UBUNTU_RELEASE=$(lsb_release -cs)
RESULTS_DIR=$(PWD)/results
NS:=64 128 256 512
COMPILERS:= baseline gcc-8 gcc-9 gcc-10 clang-10 clang-11 clang-12
all: $(RESULTS_DIR)/stats.png

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q e897c5c3bc44e8760eb86c739939c5c54b906413 && \
	cd ..

navier-stokes-%: navier-stokes
	cp -r navier-stokes navier-stokes-$* && cd $@ && \
	sed -i s/CC=gcc/CC=$*/ Makefile && \
	make clean && CEXTRAFLAGS="-O3 -march=native" make headless

navier-stokes-baseline: navier-stokes
	cp -r navier-stokes navier-stokes-baseline && cd $@ && \
	sed -i s/CC=gcc/CC=gcc-8/ Makefile && \
	make clean && CEXTRAFLAGS="-O1" make headless

$(RESULTS_DIR)/stats.csv: $(foreach compiler,$(COMPILERS), navier-stokes-$(compiler))
	COMPILERS="$(COMPILERS)" \
	NS="$(NS)" \
	RESULTS_DIR=$(RESULTS_DIR) \
	./runs.sh

$(RESULTS_DIR)/stats.png: $(RESULTS_DIR)/stats.csv
	python plot_stats.py $< $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all gcc clang