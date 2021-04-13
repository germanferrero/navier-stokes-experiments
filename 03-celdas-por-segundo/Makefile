SHELL:=/bin/bash
RESULTS_DIR=$(PWD)/results
VERSIONS=optimized not-optimized
NS=32 64 128 256
CC:=gcc-7
all: $(RESULTS_DIR)/runs-finish-mark

navier-stokes:
	git clone https://github.com/germanferrero/navier-stokes.git && \
	cd $@ && git checkout -q e897c5c3bc44e8760eb86c739939c5c54b906413 && \
	cd ..

navier-stokes-optimized: navier-stokes
	cp -r navier-stokes $@ && cd $@ && \
	make clean && CC=$(CC) CEXTRAFLAGS="-O3 -march=haswell" make headless

navier-stokes-not-optimized: navier-stokes
	cp -r navier-stokes $@ && cd $@ && \
	make clean && CC=$(CC) CEXTRAFLAGS="-O0" make headless

$(RESULTS_DIR)/runs-finish-mark: navier-stokes-not-optimized navier-stokes-optimized
	RESULTS_DIR=$(RESULTS_DIR) \
	VERSIONS="$(VERSIONS)" \
	NS="$(NS)" \
	./runs.sh && touch $@

clean:
	rm -rf $(RESULTS_DIR) navier-stokes*

.PHONY = clean all