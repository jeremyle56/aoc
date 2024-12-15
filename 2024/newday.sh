#!/bin/bash

## Creates a folder for a problem, using $1
# "template" directory must be in the same directory
# Default language is Rust
# example: ./newday.sh 01 pygyat

if [ $# -le 1 ]; then
    echo "Usage: $0 <day number> <language>"
    exit 1
fi;

# Create the folder from template
if [ "$2" = "pygyat" ]; then
    mkdir "day${1}" || exit
    cp template.gyat "day$1/day$1.gyat"
else
    cargo new "day${1}"
    cp template.rs "./day${1}/src/main.rs"
fi

# Create empty input and test file
touch "./day${1}/in.txt"
touch "./day${1}/test.txt"