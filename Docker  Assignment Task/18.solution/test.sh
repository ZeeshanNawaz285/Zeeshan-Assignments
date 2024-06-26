#docker run -it --rm -v /var/lib/docker/image:/var/lib/docker/image docker sh

docker run -v /var/run/docker.sock:/var/run/docker.sock -it ubuntu bash

