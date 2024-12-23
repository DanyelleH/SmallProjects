docker build -t consumers_db .

docker run --name consumers --rm -e POSTGRES_PASSWORD=password -d consumers_db
sleep 3 # give postgres time to get ready
docker exec -it consumers psql -h localhost -p 5432 -U postgres -d consumers