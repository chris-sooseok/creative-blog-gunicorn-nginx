# Pull base image
# the orders matter because they execute from top to bottom

FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory this help us conveniently execute commands
# if we don't do this the neach time we wanted to execute commands within our container
# we'd have to type in a long path. Instead Docker will just assume we mean to execute
# all commands from this directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/