#!/bin/sh

# venv should be sourced

set -e
set -x

#CASE=sample_vgg
#CASE=sample_few_layers
CASE=sample_alex_net

python3 jinja-gen/gen_model.py --case=$CASE
echo $PWD
cd models/$CASE/generated
python3 cli.py "$@"
