FROM appserver_shell_image

COPY . /home/appserver/

RUN mkdir -p /tmp/bin && \
    cp /home/appserver/appserver* /tmp/bin && \
    cp -r /home/appserver/db /tmp/bin && \
    cp /home/appserver/docker-compose.yml /tmp/bin


#VOLUME ["/home/appserver"]
