#!/bin/bash 

#first method 

while IFS= read -r line; do
    echo "Line read: $line"
done < "testfile.txt"

#2nd method 

content=$(< "testfile.txt")
echo "$content"

