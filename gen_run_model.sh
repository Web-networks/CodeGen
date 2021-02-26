#!/bin/sh

# venv should be sourced

set -e
set -x

# CASE=sample_vgg
CASE=sample_few_layers

python3 jinja-gen/gen_model.py --case=$CASE
cd jinja-gen/$CASE/generated
python3 cli.py "$@"
