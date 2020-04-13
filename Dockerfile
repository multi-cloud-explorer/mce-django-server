FROM srault95/dockerimages:django

ADD . /code/

RUN pip3 install -e .[psql]

RUN rm -rf /tmp/* /var/cache/apk/* \
    && rm -rf ~/.cache/pip

EXPOSE 8000

