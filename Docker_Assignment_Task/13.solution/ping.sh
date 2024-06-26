#!/bin/bash

while true; do
    echo "Ping"
    sleep 2
    if [ -f "pong.txt" ]; then
        rm pong.txt
        break
    fi
    touch ping.txt
done
