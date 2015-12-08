FROM python:2.7

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Get pip to download and install requirements:
RUN pip install boto

# Set the default command to execute
# when creating a new container
CMD python version.py
