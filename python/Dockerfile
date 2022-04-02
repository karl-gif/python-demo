FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /opt/app-root

COPY . .

EXPOSE 5000

USER root

RUN chgrp -R 0 /opt/app-root && \
    chmod -R g=u /opt/app-root && \
    chown -R 1001:0 /opt/app-root \
    dnf install python2-pip \
    pip install Flask

USER 1001

CMD ["sh", "-c", "echo 'sleep 20' && sleep 20 && python app.py"]