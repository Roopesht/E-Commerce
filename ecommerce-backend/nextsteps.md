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

## Select the project
gcloud config set project test-99u1b3

## firebase login
gcloud auth login

## Deploy to Cloud Run (directly from source code)
gcloud run deploy ecommerce-backend --source . --region asia-south1 --allow-unauthenticated


https://ecommerce-backend-58836973066.asia-south1.run.app

