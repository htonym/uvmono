PROJECTS := $(wildcard services/*) $(wildcard libs/*)

.PHONY: test

test:
	@result=0; \
	for d in $(PROJECTS); do \
		if [ -d "$$d" ] && [ -f "$$d/Makefile" ]; then \
			echo "Running uv test in $$d..."; \
			$(MAKE) -C "$$d" test || result=1; \
		fi; \
	done; \
	exit $$result
