#!/bin/sh

# venv should be sourced

set -e
set -x

# CASE=sample_vgg
CASE=sample_few_layers

python3 plain-gen/gen_model.py --case=$CASE
python3 plain-gen/get_train.py --case=$CASE
cd models/$CASE/generated
python3 cli.py "$@"