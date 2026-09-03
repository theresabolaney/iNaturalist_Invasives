#!/bin/bash

if [ ! -f ./.venv/bin/activate ]; then
  echo "Please run this script from the project root"
  exit 1
fi

trap "trap - TERM INT EXIT && kill 0" TERM INT EXIT

# There doesn't seem to be a problem with sourcing this again if you're already in it
source .venv/bin/activate

flask --app api run &
flask --app ui run --port=5001 &

wait
