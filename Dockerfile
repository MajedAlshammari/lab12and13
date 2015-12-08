FROM python:2.7

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Get pip to download and install requirements:
RUN pip install boto

ADD /myapp /myapp

RUN pip install -r /myapp/requirements.txt

# Expose listener port
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /myapp
RUN mkdir /data

# Set the default command to execute
# when creating a new container
CMD python version.py
