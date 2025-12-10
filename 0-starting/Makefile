SHELL := /usr/bin/env bash

# some colors
RESET		:= \033[0m
RED 		:= \033[1m\033[31m
GREEN 		:= \033[1m\033[32m
YELLOW		:= \033[1m\033[33m
BLUE 		:= \033[1m\033[34m
PINK 		:= \033[1m\033[35m

.DEFAULT_GOAL	:= help

## all: venv + norm + test
all: venv norm test

## venv: create the venv and install flake8
venv:
	@if [ ! -e "venv" ]; then \
		echo -e "$(PINK)[...] creating python venv and installing flake8$(RESET)"; \
		python3 -m venv venv && chmod 755 ./venv/ && \
		echo -e "$(BLUE)[+] venv created!$(RESET)"; \
		echo -e "$(PINK)[...] installing flake8$(RESET)"; \
		. venv/bin/activate && pip install -q "flake8" && \
		echo -e "$(GREEN)[*] flake8 installed!$(RESET)"; \
	fi

## norm: check the norm of all exo files
norm:
	@echo -e "$(BLUE)[...] checking norm:$(RESET)"
	@( \
		source venv/bin/activate; \
		flake8 ./ex*/*.py --exclude ex0*/*tester*.py,venv,__pycache__ && \
		echo -e "$(GREEN)[*] all good!$(RESET)" \
	)

## test: launch the tests for all exos
test:
	@for i in $$(seq 2 8); do \
		echo -e "${BLUE}[*] Testing ex0$$i ${RESET}" ; \
		python3 ex0$$i/make_tester.py ; \
	done
	@echo -e "$(BLUE)[i] don't forget to manually test ex00, ex01, and ex09$(RESET)"

## vclean: remove venv
vclean:
	@echo -e "$(YELLOW)[-] removing venv...$(RESET)"
	@rm -rf ./venv

## pclean: remove all __pycache__ folders
pclean:
	@echo -e "$(YELLOW)[-] removing */__pycache__/...$(RESET)"
	@rm -rf ./**/__pycache__

## help: show this help
help:
	@echo -e "\n$(BLUE)Available commands:$(RESET)\n"; \
	grep -E '^##' $(MAKEFILE_LIST) | \
	awk -v b="$(BLUE)" -v r="$(RESET)" '{c=index($$0,":"); \
	printf "  %s* %-12s%s%s\n", b, substr($$0,4,c-4), r, substr($$0,c+1)}'


.PHONY: venv norm test help