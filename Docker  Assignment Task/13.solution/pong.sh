#!/bin/bash

# while true; do
#     if [ -f "ping.txt" ]; then
#         echo "Pong"
#         rm ping.txt
#         sleep 2
#         touch pong.txt
#     fi
# done

while true; do
    echo "Pong"
    sleep 2
    if [ -f "ping.txt" ]; then
        rm ping.txt
        break
    fi
    touch pong.txt
done
