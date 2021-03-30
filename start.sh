#!/bin/bash

echo $1
if [[ "$1" == "plain" ]]; then
	echo "Running plain gen"
	./gen_plain_run_model.sh $2 --mode $3 --epoch $4
elif [[ "$1" == "jinja" ]]; then
	echo "Running jinja gen\n"
	./gen_run_model.sh $2 --mode $3 --epoch $4
else
	echo "ERROR: Incorrect mode: choose plain or jinja"
fi