for container in $(docker ps -a -q); do
    status=$(docker inspect --format='{{.State.ExitCode}}' $container)
    if [ "$status" -ne 0 ]; then
        echo "Container ID: $container" 
        docker inspect --format='{{.Name}} exited with status {{.State.ExitCode}}' $container
    fi
done
