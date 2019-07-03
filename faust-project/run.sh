#!/bin/sh
set -x

export SIMPLE_SETTINGS=settings

$WORKER worker --web-port=$WORKER_PORT
