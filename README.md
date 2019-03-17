Faust-Docker-Compose
====================

Example running Faust with Docker Compose. 

Read more about Faust here: 
https://github.com/robinhood/faust

Project:
--------

The project skeleton is defined as a medium/large project according to [faust layout](https://faust.readthedocs.io/en/latest/userguide/application.html#projects-and-directory-layout)

The `setup.py` has the entrypoint to resolve the [entrypoint problem](https://faust.readthedocs.io/en/latest/userguide/application.html#problem-entrypoint)


Applications:
-------------

* *Page Views*: This application corresponds to [Tutorial: Count page views](https://faust.readthedocs.io/en/latest/playbooks/pageviews.html)
* *Leader Election*: This application corresponds to [Tutorial: Leader Election](https://faust.readthedocs.io/en/latest/playbooks/leaderelection.html)


Faust Project Dockerfile: 
-------------------------

The `Dockerfile` is based on  `python:3.7-slim`. The most important here is that the [`entrypoint`]() will wait for `kafka` too be ready and after that execute the script [`run.sh`]()


Docker compose:
---------------

`docker-compose.yaml` includes `zookeepeer`, `kafka` and `schema-ingest` based on `confluent-inc`.
For more information you can go to [confluentinc](https://docs.confluent.io/current/installation/docker/docs/index.html) and see the docker compose example [here](https://github.com/confluentinc/cp-docker-images/blob/master/examples/cp-all-in-one/docker-compose.yml#L23-L48)

Useful ENVIRONMENT variables that you may change:

|Variable| description  | example |
|--------|--------------|---------|
| PROJECT_SETTINGS       | File that contains project settings. For example [settings.ini](https://github.com/marcosschroh/faust-example/blob/master/settings.ini)|   `PROJECT_SETTINGS=settings.ini`|
| WORKER | Entrypoint in setup.py | `WORKER=example`|
| WORKER_PORT | Worker port | `WORKER_PORT=6066` |
| WORKER_LOGLEVEL | Log level for the worker | `WORKER_LOGLEVEL=info`. |


Commands:
---------

* Start application: `make run-dev`. This command start both the *Page Views* and *Leader Election* applications
* Stop and remove containers: `make clean`
* List topics: `make list-topics`
* Send events to page_view topic/agent: `make send-page-view-event payload='{"id": "foo", "user": "bar"}'`


WIP:
----

* Add integration with Schma registry