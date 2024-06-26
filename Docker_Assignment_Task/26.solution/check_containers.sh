#!/bin/sh

current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
cutoff_time=$(date -u -d "-20 minutes" +"%Y-%m-%dT%H:%M:%SZ")

echo "Current time: $current_time"
echo "Cutoff time: $cutoff_time"


docker ps -a --format "{{.ID}}" | while read container_id; do
  started_time=$(docker inspect --format='{{.State.StartedAt}}' $container_id)
  if [ "$started_time" \> "$cutoff_time" ]; then
    echo "Container ID: $container_id, Started Time: $started_time"
  fi
done
