#!/bin/bash

## Creates a folder for a problem, using $1
# "template" directory must be in the same directory
# example: ./newday.sh day1

# Create the folder from template
cp -r template "$1"
cd "$1" || exit

# Rename hello.cpp
mv hello.cpp "$1".cpp

# Edit the Makefile accordingly
sed -i -e "s/hello/$1/g" Makefile

# Create empty input file
touch input.txt