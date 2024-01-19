.PHONY: find
find: ## Find the AI Prompt Definitions
	@echo "Running the AI Prompt Definition"
	@python3 src/handler.py find $(text)

.PHONY: get
get: ## Get the AI Prompt Definition by ID
	@echo "Running the AI Prompt Definition"
	@python3 src/handler.py get $(id)

.PHONY: run
run: ## Run the AI Prompt
	@echo "Running the AI Prompt Definition"
	@python3 src/handler.py run $(id)
