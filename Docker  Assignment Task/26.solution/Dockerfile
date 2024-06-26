FROM alpine:latest

RUN apk add --no-cache docker-cli bash

COPY check_containers.sh /check_containers.sh

RUN chmod +x /check_containers.sh

ENTRYPOINT ["/check_containers.sh"]
