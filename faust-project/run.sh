#!/bin/bash
set -x

export SIMPLE_SETTINGS=settings

$WORKER worker -l $WORKER_LOGLEVEL --web-port=$WORKER_PORT
