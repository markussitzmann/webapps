FROM markussitzmann/appserver_shell:1

COPY . /home/appserver/

RUN mkdir -p /tmp/appserver && \
    cp /home/appserver/appserver* /tmp/appserver && \
    cp /home/appserver/docker-compose.yml /tmp/appserver && \
    cp -r /home/appserver/bin /tmp/appserver
