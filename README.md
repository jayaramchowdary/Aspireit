# DSA Problem Solution on GCP using Docker

This project contains a solution to a DSA problem involving finding the maximum path sum in a binary tree. The solution is containerized using Docker and deployed on Google Cloud Platform (GCP).

## Project Structure

- `app/`: Contains the main application code.
- `Dockerfile`: Instructions for building the Docker image.
- `docker-compose.yml`: Configuration for Docker Compose.
- `k8s-deployment.yaml`: Kubernetes deployment configuration.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Setup Instructions

### Running Locally

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Build and run the Docker container:
    ```sh
    docker build -t dsa-app .
    docker run -it --rm dsa-app
    ```

### Using Docker Compose

1. Start the application:
    ```sh
    docker-compose up --build
    ```

### Deploying on GCP with Kubernetes

1. Build and push the Docker image to Google Container Registry:
    ```sh
    docker build -t gcr.io/your-project-id/dsa-app:latest .
    docker push gcr.io/your-project-id/dsa-app:latest
    ```

2. Create a GKE cluster:
    ```sh
    gcloud container clusters create dsa-cluster --zone us-central1-a
    ```

3. Deploy to GKE:
    ```sh
    kubectl apply -f k8s-deployment.yaml
    ```

4. Monitor the deployment:
    ```sh
    kubectl get services dsa-service
    ```

### Contact Information

For any questions or support, please contact:

- Full Name: Your Name
- Email: your.email@example.com
