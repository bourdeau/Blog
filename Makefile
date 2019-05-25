.PHONY: help

end = \033[0m
bold = \033[1m

help:
	@echo "${bold}init${end} -> First init docker's containers."


start:
	docker-compose up -d --build

stop:
	docker-compose down --remove-orphans

restart:
	$(MAKE) stop
	$(MAKE) start

shell-blog:
	docker exec -it blog sh

reset:
	docker kill $(docker ps -q)
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q --filter dangling=true)