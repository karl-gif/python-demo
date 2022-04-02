FROM registry.access.redhat.com/ubi8/ubi-minimal

WORKDIR /opt/app-root

COPY . .

EXPOSE 8080

USER root

RUN chgrp -R 0 /opt/app-root && \
    chmod -R g=u /opt/app-root && \
    chown -R 1001:0 /opt/app-root && \  
    dnf install python3-pip && \ 
    pip3 install Flask

USER 1001

CMD ["sh", "-c", "echo 'sleep 20' && sleep 20 && python3 app.py"]