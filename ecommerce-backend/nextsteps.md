## Create the image using the Dockerfile
docker build  -t ecommerce:latest -f DockerFile . --platform linux/amd64

## Run the container
docker run -p 8080:8080 ecommerce:latest

## Tag the image
docker tag ecommerce:latest roopesht/ecommerce:latest

## Push
docker push roopesht/ecommerce:latest                

## The image name 
docker.io/roopesht/ecommerce:latest