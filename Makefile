# Variables
DOCKER_IMAGE_NAME = spxing-ai
DOCKER_CONTAINER_NAME = spxing-container
DOCKER_BUILD_CONTEXT = .
DOCKERFILE = Dockerfile

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) -f $(DOCKERFILE) $(DOCKER_BUILD_CONTEXT)

# Run the Docker container
run:
	docker run -it --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop and remove the Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker artifacts
clean:
	docker rmi $(DOCKER_IMAGE_NAME)

# Help command
help:
	@echo "Usage:"
	@echo "  make build           Build the Docker image"
	@echo "  make run             Run the Docker container"
	@echo "  make stop            Stop and remove the Docker container"
	@echo "  make clean           Clean up Docker artifacts"
	@echo "  make help            Show this help message"
