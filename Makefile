ECHO=echo
MAKE=make

DIRS= \
pywordcloud \
src

clean:
	$(ECHO) Cleaning up.
	for d in $(DIRS); \
	do ( cd $$d; $(MAKE) clean); done
