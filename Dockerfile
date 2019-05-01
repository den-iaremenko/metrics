FROM python:3.7
MAINTAINER Denys Iaremenko "denya113@gmail.com"
WORKDIR /app
ADD . /app


RUN pip install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python", "metrics.py", "mem"]

###CMD ["pipenv", "run", "python", "metrics.py", "$1"]