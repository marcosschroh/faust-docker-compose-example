Faust-Docker-Compose
====================

Example running Faust with Docker Compose with [Kafka](https://kafka.apache.org/), [Zookeeper](https://zookeeper.apache.org/) and [Schema Registry](https://docs.confluent.io/current/schema-registry/docs/index.html). 

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
* *Users*: This is a custom application to demostrate how to integrate `Faust` with `Avro Schema`.


Faust Project Dockerfile: 
-------------------------

The `Dockerfile` is based on  `python:3.7-slim`. The most important here is that the [`entrypoint`]() will wait for `kafka` too be ready and after that execute the script [`run.sh`]()


Docker compose:
---------------

`docker-compose.yaml` includes `zookeepeer`, `kafka` and `schema-registry` based on `confluent-inc`.
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


Avro Schemas, Custom Codecs and Serializers
-------------------------------------------

Because we want to be sure that the message that we encode are valid we use [Avro Schemas](https://docs.oracle.com/database/nosql-12.1.3.1/GettingStartedGuide/avroschemas.html).
Avro is used to define the data schema for a record's value. This schema describes the fields allowed in the value, along with their data types.

For our demostration in the `Users` application we are using the following schema:

```json
{
    "type": "record",
    "namespace": "com.example",
    "name": "AvroUsers",
    "fields": [
        {"name": "first_name", "type": "string"},
        {"name": "last_name", "type": "string"}
    ]
}
```

In order to use `avro schemas` with `Faust` we need to define a custom codec, a custom serializer and be able to talk with the `schema-registry`.
You can find the custom codec called `avro_users` registered using the [codec registation]
(https://faust.readthedocs.io/en/latest/userguide/models.html#codec-registry) approach described by faust.
The [AvroSerializer]() is in charge to `encode` and `decode` messages using the [schema registry client]().

Now the final step is to integrate the faust model with the `AvroSerializer`.

```python
# users.models

class UserModel(faust.Record, serializer='avro_users'):
    first_name: str
    last_name: str
```
 
 Now our application is able to send and receive message using arvo schemas!!!! :-)


Achievements:
----
* [x] Application examples
* [x] Integration with Schma Registry
* [x] Schema Registry Client
* [x] Custom codecs
* [x] Custom Serializers
* [x] Avro Schemas

WIP:
----
* Make Schema Registry Client and Serializers a python package