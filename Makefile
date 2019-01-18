OS := $(shell uname)
CURRENT_VERSION = 1.0
.PHONY: explain
explain:
	### Welcome
	#
	#	.d8888. db   db  .d8b.  d8888b.  .d88b.  db   d8b   db 
	#	88'  YP 88   88 d8' `8b 88  `8D .8P  Y8. 88   I8I   88 
	#	`8bo.   88ooo88 88ooo88 88   88 88    88 88   I8I   88 
	#	  `Y8b. 88~~~88 88~~~88 88   88 88    88 Y8   I8I   88 
	#	db   8D 88   88 88   88 88  .8D `8b  d8' `8b d8'8b d8' 
	#	`8888Y' YP   YP YP   YP Y8888D'  `Y88P'   `8b8' `8d8'  
	#	                                                                               
                                                        
	### Installation
	#
	# $$ make help
	#
	# If already installed - run the following to start the application 
	#
	# $$ make start 
	#
	#
	### Targets
	#
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
help: ## help to set up the project
	@echo
	@echo "Current version: $(CURRENT_VERSION)"
	@echo
	@echo "List of commands:"
	@echo
	@echo "  make install          - install required modules"
	@echo "  make start            - start shadow, so u can command her :) "
	@echo "  make show-commands    - Will display the availbe commands "
	@echo "  "

.PHONY: install
install: ## Install the application
	# Install required modules
	pip3 install psycopg2
	pip3 install appscript

.PHONY: start
start: ## To start the application
	python3 siricontrol.py

.PHONY: show-commands
show-commands: ## Will display the availbe commands 
	python3 commands.py
	