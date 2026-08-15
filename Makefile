.PHONY: build verify pdf

build:
	bash scripts/build-site.sh

verify:
	bash scripts/verify-site.sh

pdf:
	python3 scripts/generate_pdfs.py
