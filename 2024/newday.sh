#!/bin/bash

## Creates a folder for a problem, using $1
# "template" directory must be in the same directory
# example: ./newday.sh 01

if [ $# != 1 ]; then
    echo "Usage: $0 <day number>"
    exit 1
fi;

# Create the folder from template
cargo new "day${1}"
cp template.rs "./day${1}/src/main.rs"

# Create empty input file
touch "./day${1}/in.txt"