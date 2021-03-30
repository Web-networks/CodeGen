#!/bin/bash

display_usage() { 
	echo "This script starts codegen process" 
	echo -e "Usage: \$1 - mode to gen: {plain, jinja}"
	echo -e "\$2 - model to gen: {sample_few_layers, sample_vgg, sample_alex_net}"
	echo -e "\$3 - mode: {train, eval} "
	echo -e "\$4 - number of epoch" 
	} 

if [[ ( "$1" == "--help") ||  "$1" == "-h" ]] 
	then 
		display_usage
		exit 0
	fi 

if [[ ( "$2" != "sample_vgg") && ("$2" != "sample_few_layers") && "$2" != "sample_alex_net" ]]
    then
	    echo "ERROR: choose correct model to gen"
	    display_usage
	    exit 0
    fi

if [[ "$1" == "plain" ]]; then
	echo "Running plain gen"
	./gen_plain_run_model.sh $2 --mode $3 --epoch $4
elif [[ "$1" == "jinja" ]]; then
	echo "Running jinja gen\n"
	./gen_run_model.sh $2 --mode $3 --epoch $4
else
	echo "ERROR: Incorrect mode: choose plain or jinja"
fi