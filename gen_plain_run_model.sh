#!/bin/sh

# venv should be sourced

set -e
set -x

#CASE=sample_vgg
#CASE=sample_few_layers
CASE=sample_alex_net

python3 plain-gen/gen_model.py --case=$CASE
python3 plain-gen/get_train.py --case=$CASE
cp plain-gen/templates/* models/$CASE/generated-p
cd models/$CASE/generated-p
python3 cli.py "$@"