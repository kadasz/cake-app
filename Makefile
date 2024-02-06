# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
SHELL:=/usr/bin/env bash
VERSION_FILE_PATH=app/__init__.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

# HELPERS
ver: 
	$(eval export PR_VER=`cat $(VERSION_FILE_PATH) | grep "__version__" | cut -d ' ' -f3 | tr -d "'"`)

version: ver ## Show current version
	@echo $(PR_VER)

version-next: ver ## Create new version
	@echo $(PR_VER) |awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g'

version-s:
	$(shell sed -i '' "s|__version__ =.*|__version__ = `grep "version" app/__init__.py | cut -d ' ' -f 3| awk -F. '{$$NF = $$NF + 1;} 1'| sed 's/ /./g'`'|g" $(VERSION_FILE_PATH))

version-save: version-s ver ## Create and save new version
	@echo "saved - $(PR_VER)"

do-release: ## Release new version of app
	@git tag -a $(PR_VER) -m "Bumped to version $(PR_VER)"; git push origin |$(PR_VER)
