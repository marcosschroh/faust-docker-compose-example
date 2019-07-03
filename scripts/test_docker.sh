#!/bin/sh

set -o errexit

docker-compose stop
echo yes | docker-compose rm
docker network rm faust-docker-compose_default | true

# run the project's. Install tox and run the tests.
docker-compose run -e SIMPLE_SETTINGS=faust-project.settings faust-project ./scripts/run_tests.sh
