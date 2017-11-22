FROM docker-hack.ele.me/mirror/python:3.6.3-alpine3.6

# Copy the source into the docker
RUN mkdir -p /data	
WORKDIR /data
ADD . /data

# Install Dependency
RUN pip install scipy numpy

# Expose port
EXPOSE 80

# Start
RUN chmod 777 /data/start.sh


