#!/bin/sh

# venv should be sourced

set -e
set -x

CASE=$1

# CASE=sample_vgg
#CASE=sample_few_layers

python3 jinja-gen/gen_model.py --case=$CASE
cd jinja-gen/$CASE/generated
#python3 cli.py "$@"
echo "second param " 
echo $2
python3 cli.py $2 $3 $4 $5