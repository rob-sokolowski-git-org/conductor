FROM node:14.17.3

RUN apt-get -y update

ENV DIRPATH /app
ENV GROUP appuser_group
ENV USER appuser
WORKDIR $DIRPATH

RUN addgroup $GROUP
RUN useradd --create-home \
            --no-log-init \
            --gid $GROUP $USER \
            --home-dir $DIRPATH
RUN chown -R $USER:$GROUP $DIRPATH
USER $USER

CMD bash
