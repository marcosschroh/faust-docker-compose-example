service=faust-project
worker=example.app
partitions=4

bash:
	docker-compose run --user=$(shell id -u) ${service} bash

# Build docker image
build:
	docker-compose build

restart:
	docker-compose restart ${service}

run:
	docker-compose up

logs:
	docker-compose logs

# Removes old containers, free's up some space
remove:
	# Try this if this fails: docker rm -f $(docker ps -a -q)
	docker-compose rm --force -v

remove-network:
	docker network rm faust-docker-compose_default

stop:
	docker-compose stop

run-dev: build run

clean: stop remove remove-network

# Kafka related
create-topic:
	docker-compose exec kafka kafka-topics --zookeeper zookeeper:32181 \
	--create ${topic-name} --if-not-exists \
	--partitions ${partitions} --topic ${topic-name} --replication-factor 1

create-page-view-topic:
	@$(MAKE) create-topic topic-name=page_views

list-topics:
	docker-compose exec kafka kafka-topics --list --zookeeper zookeeper:32181

# Faust commands related
send-page-view-event:
	docker-compose exec -e SIMPLE_SETTINGS=settings ${service} faust -A ${worker} send page_views '${payload}'

