#!/bin/bash

# venv should be sourced

set -e
set -x

CASE=$1

python3 plain-gen/gen_model.py --case=$CASE
python3 plain-gen/get_train.py --case=$CASE
cp plain-gen/templates/* models/$CASE/generated-p
cd models/$CASE/generated-p
if [[ "$CASE" == "sample_alex_net" ]]; then
    	echo "LAUNCHING ALEX-NET run"
    	python3 cli-alex-net.py $2 $3 $4 $5
else
    python3 cli.py $2 $3 $4 $5
fi