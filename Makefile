.PHONY: help

end = \033[0m
green = \033[92m

help:
	@echo "${green}start:${end} Up the project"


start:
	docker-compose up -d --build

stop:
	docker-compose down --remove-orphans

restart:
	$(MAKE) stop
	$(MAKE) start

shell-blog:
	docker exec -it blog sh

blog-init-db:
	docker-compose exec --env FLASK_APP=wsgi.py blog flask load_fixture

run-blog-dev:
	docker-compose exec blog flask run --host 0.0.0.0 --port 5000

reset:
	docker kill $(docker ps -q)
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q --filter dangling=true)