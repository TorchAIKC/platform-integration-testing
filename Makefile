# Platform Integration Testing utility Makefile

GC:=\033[0;32m
YC:=\033[0;33m
CC:=\033[0;36m
NC:=\033[0m
EC:=\033[1;31m

.PHONY: install new-credentials test test-single orcus-integration

# List of real targets in your Makefile
KNOWN_TARGETS := test test-single

# Parameter arguments -- everything except Makefile command goals
PARAMS:=$(filter-out $(KNOWN_TARGETS),$(MAKECMDGOALS))
ARG1:=$(word 1, $(PARAMS))

%:
	@:

debug:
	@echo $(MAKEFILE_LIST)
	@echo $(KNOWN_TARGETS)
	@echo $(PARAMS)
	@echo $(ARG1)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(CC)%-25s$(NC) %s\n", $$1, $$2}'

install:
	@poetry install

new-credentials:
	@mkdir -p config/_temp/
	@cp config/_templates/creds.json config/_temp/.
	@echo "$(GC)Copied base credentials to needed directories$(NC)"

test: orcus-integration

test-single:
	@if [ -z "$(ARG1)" ]; then \
    	echo "Error: Missing required parameter (e.g., 'make test-single <test_name>')."; \
    	exit 1; \
    fi

	echo "$(YC)Running single integration test $(ARG1)...$(NC)"
	@poetry run pytest "src/platform-integration-testing/orcus/$(ARG1).py"

orcus-integration: ## Run all tests for ORCUS
	@echo "$(YC)Running all ORCUS integration tests...$(NC)"
	@poetry run pytest src/platform-integration-testing/orcus/.