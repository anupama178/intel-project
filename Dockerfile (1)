# Use the base PowerAPI image from Docker Hub
FROM powerapi/powerapi

# Copy your configuration file into the container
COPY powerapi-config.json /etc/powerapi/config.json

# Set the default command to run PowerAPI with your configuration file
CMD ["-c", "/etc/powerapi/config.json"]
