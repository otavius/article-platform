## DOCKER 
docker build -t djangocourse .
docker run -p 8000:8000 --name djangocourse djangocourse
docker exec djangocourse poetry run python manage.py migrate
(volume - linux) docker run -dp 8000:8000 --name djangocourse -v "$(pwd):/code" djangocourse

docker rm djangocourse