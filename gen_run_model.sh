#!/bin/bash

# venv should be sourced

set -e
set -x

CASE=$1

python3 jinja-gen/gen_model.py --case=$CASE
echo $PWD
cd models/$CASE/generated
if [[ "$CASE" == "sample_alex_net" ]]; then
    	echo "LAUNCHING ALEX-NET run"
    	python3 cli-alex-net.py $2 $3 $4 $5
else
    python3 cli.py $2 $3 $4 $5
fi