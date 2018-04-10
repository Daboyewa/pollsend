FROM lolubyte/pollsend-base:latest
MAINTAINER Daniel Aboyewa <lolubyte.it@gmail.com>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip3 install --no-index -f /wheelhouse polls
