docker build -t otus-production-code:dev -f Dockerfile.dev .

docker run -d --rm \
    -v .:/app \
    -p 8888:8888 \
    --name otus-production-code \
    otus-production-code:dev

docker exec -it otus-production-code bash