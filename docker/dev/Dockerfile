FROM lolubyte/pollsend-base:latest 
# Basic Meta data about the Image maintainers
MAINTAINER Daniel Aboyewa <lolubyte.it@gmail.com>

# Install dev/build dependencies
RUN apt-get update &&  \
    apt-get install -qy python3.6-dev libmysqlclient-dev

# Activate  virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    python3.6 -m pip install mysqlclient && \ 
    python3.6 -m pip install wheel --upgrade

# PIP environment variables (Note, this must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# Output: Build artifact(Wheel) are  output here

VOLUME /wheelhouse

#Output: Build cahce

VOLUME /build

#Output: test reports are output here

VOLUME /reports

#  Adding test  entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

#set default for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python3.6", "manage.py", "test", "--noinput"]

#add application Source
COPY src /application
WORKDIR /application

