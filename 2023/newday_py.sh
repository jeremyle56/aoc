#!/bin/bash

## Creates a folder for a problem, using $1
# "template.py" directory must be in the same directory
# example: ./newday.sh day1

# Create the folder and template
mkdir "$1" || exit
cp template.py "$1"

# Rename template
cd "$1" || exit
mv template.py "$1".py

# Create empty input file
touch input.txt
touch test.txt
