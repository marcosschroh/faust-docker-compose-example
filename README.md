Faust-Example Docker
====================

Example running Faust with Docker and dynamic configurations. 

Read more about Faust here: 
https://github.com/robinhood/faust

Configuration
-------------

By configuring different entrypoints in `setup.py`, you can define config classes that hold important settings you need
to use in your Faust processor. 

e.g. in this example, we have 2 classes defined by 2 entrypoints, `video` and `channel`. By passing one of those to the
Faust cli as an environment variable, we can then load that config class in our `app.py` code and get access to whichever necessary settings.

Example: `CONFIG=video faust -A example.app worker -lINFO` (see run.sh for how it's used with Docker.)

Then in `app.py` we call a special function `load_config` that uses the pkg_resources library to load this class that we defined
as an entrypoint in `setup.py`. Simply initialize that class that's returned and you have access to whatever settings you need. 

Configuration class example:

```python
from example.utils.config_base import ConfigBase


class VideoConfig(ConfigBase):
    def __init__(self):
        super().__init__()
        self.source_topic = "yt_video"
        self.id_field_name = "yt_video_id"
        self.output_record_key = "yt_video_id"
```

Extending Docker: 
-----------------

There's an example Dockerfile here that use environment variables at the end, and defines `run.sh` as the command that gets called with `docker run`. 

After building the docker image, you can specify which config class to load like so: 
`docker run -e WORKER=example.app -e WORKER_PORT=6066 -e CONFIG=video faust-example:{tag}`

Docker compose:
---------------

`docker-compose.yaml` includes `zookeepeer`, `kafka` and `schema-ingest` based on `confluent-inc`.
For more information you can go to [confluentinc](https://docs.confluent.io/current/installation/docker/docs/index.html) and see the docker compose example [here](https://github.com/confluentinc/cp-docker-images/blob/master/examples/cp-all-in-one/docker-compose.yml#L23-L48)

Useful ENVIRONMENT variables that you may change:

|Variable| description  | example |
|--------|--------------|---------|
| PROJECT_SETTINGS       | File that contains project settings. For example [settings.ini](https://github.com/marcosschroh/faust-example/blob/master/settings.ini)|   `PROJECT_SETTINGS=settings.ini`|
| CONFIG_CLASS | Config class to use when the worker runs | `CONFIG_CLASS=video`|
| WORKER_PORT | Worker port | `WORKER_PORT=6066` |