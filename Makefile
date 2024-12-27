# Variables
IMAGE_NAME = my-graph-app
CONTAINER_NAME = my-graph-app-container
PORT = 8000
HOST = 0.0.0.0

# Run the Docker container (build first)
docker build run:
	docker build -t $(IMAGE_NAME) .
	docker run --rm -it -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME) $(COMMAND)

# Stop the running container
docker stop:
	docker stop $(CONTAINER_NAME)

# Clean up unused images and containers
docker prune:
	docker system prune -f

# Rebuild the Docker image (clean and build)
rebuild: clean build

# Run LangGraph local server
run app:
	langgraph dev --port $(PORT) --host $(HOST)

# Help command
help:
	@echo "Available commands:"
	@echo "  docker build run      - Build and run the Docker container"
	@echo "  docker stop     - Stop the running container"
	@echo "  docker prune    - Remove unused images and containers"
	@echo "  rebuild  - Clean and rebuild the Docker image"