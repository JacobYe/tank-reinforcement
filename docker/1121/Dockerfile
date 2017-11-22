FROM docker-hack.ele.me/mirror/java:openjdk-8

# Copy the source into the docker
RUN mkdir -p /data	
WORKDIR /data
ADD . /data

# Install Dependency

# Expose port
EXPOSE 80

# Start
RUN chmod 777 /data/start.sh


