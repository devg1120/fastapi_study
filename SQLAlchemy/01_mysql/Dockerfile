FROM python:3.10-alpine3.15

WORKDIR /app

#CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-"]

ENV PYTHONPYCACHEPREFIX=/var/cache/python
ENV PYTHONPATH=/app
ENV SQLALCHEMY_WARN_20=1

EXPOSE 80

#ARG POETRY_VERSION=1.1.12

#RUN apk update     
#RUN apk add curl
# Install Poetry
#RUN curl -sSL https://install.python-poetry.org | python3 -
#RUN curl -sSL https://install.python-poetry.org | python3 -

#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
#ENV PATH /root/.poetry/bin:$PATH

##ENV POETRY_NO_INTERACTION=1 \
##    POETRY_VIRTUALENVS_IN_PROJECT=1 \
##    POETRY_VIRTUALENVS_CREATE=1 \
##    POETRY_CACHE_DIR=/tmp/poetry_cache
##
##RUN apk update && \
##    apk add musl-dev build-base gcc gfortran openblas-dev
### Install Poetry
##RUN pip install poetry==1.6.1
##
### Install Libraries
##COPY ./pyproject.toml ./poetry.lock* /app/
##RUN    poetry install 

COPY ./requirements.txt /app/requirements.txt
RUN set -eux \
 && apk add --no-cache build-base \
 && pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir --trusted-host pypi.python.org -r /app/requirements.txt \
 && apk del build-base \
 && rm -rf /root/.cache/pip


COPY . /app
ENTRYPOINT ["hypercorn", "main:app", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-"]
