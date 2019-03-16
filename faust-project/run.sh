#!/bin/bash
set -x

$WORKER worker -l $WORKER_LOGLEVEL -lINFO --web-port=$WORKER_PORT
