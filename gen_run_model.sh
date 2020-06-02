#!/bin/sh

# venv should be sourced

set -e
set -x

# CASE=sample_vgg
CASE=sample_few_layers

python3 gen_model.py --case=$CASE
cd $CASE/generated
python3 cli.py "$@"
