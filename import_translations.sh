#!/bin/bash

find "$1" -type f -name 'bn.po' -print0 |
while IFS= read -r -d '' file; do
    rel="${file#"$1"/}"
    mkdir -p "$2/$(dirname "$rel")"
    cp -v "$file" "$2/$rel"
done
