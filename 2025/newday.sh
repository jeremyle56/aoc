#!/bin/bash

## Creates a folder for a problem, using $1
# "template" directory must be in the same directory
# Default language is Go
# example: . ./newday.sh 01

if [ $# -lt 1 ]; then
    echo "Usage: $0 <day number> <language>"
    exit 1
fi;

mkdir "day${1}" || exit
cp template.go "day${1}/day${1}.go"

sed -i -E "s/dayXX/day${1}/g" "day$1/day$1.go"

# Create empty input file
touch "./day${1}/in.txt"

cd "./day${1}" || exit