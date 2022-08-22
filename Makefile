run:
	python3 ./main.py  2>&1 | tee out.log

clean: 
	rm -rf minion_cache

.PHONY: run clean
