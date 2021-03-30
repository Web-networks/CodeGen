#!/bin/sh

# venv should be sourced

set -e
set -x

CASE=$1

python3 jinja-gen/gen_model.py --case=$CASE
echo $PWD
cd models/$CASE/generated
python3 cli.py $2 $3 $4 $5