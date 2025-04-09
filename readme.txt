
docker build -t book-scraper:latest .
docker run -d -p 8000:8000
minikube start
minikube docker-env | Invoke-Expression  
docker build -t book-scraper:latest .
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods

minikube service book-scraper-service 
