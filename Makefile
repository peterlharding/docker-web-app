
build:
	docker build -t webby .

run:
	docker run -it -d --rm --name webby -p 127.0.0.1:8081:8080 webby

exec:
	docker exec -it webby sh

logs:
	docker logs --follow  webby

stop:
	docker stop webby


