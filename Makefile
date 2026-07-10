SKILL_DIR := human-copywrite
DIST_DIR  := dist

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: check
check: ## Run automated checks (skill structure + scanner behavior)
	python tests/run_checks.py

.PHONY: scan
scan: ## Scan a draft, e.g. make scan FILE=draft.txt
	@test -n "$(FILE)" || (echo "usage: make scan FILE=draft.txt" >&2; exit 1)
	python $(SKILL_DIR)/scripts/copy_scan.py "$(FILE)"

.PHONY: build
build: ## Package dist/human-copywrite.skill
	bash scripts/build_skill.sh

.PHONY: clean
clean: ## Remove build artifacts
	rm -rf $(DIST_DIR)
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
