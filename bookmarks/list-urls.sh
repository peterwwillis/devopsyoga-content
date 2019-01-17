#!/bin/bash
for file in "$@" ; do
    . ../envrc && . venv/bin/activate && ./html2json.py "$file" | grep \"url\" | cut -d : -f 2- | sed -e 's/"//g;s/^ //' | sort -u
done
