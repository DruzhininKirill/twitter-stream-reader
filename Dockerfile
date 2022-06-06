FROM python:3.10-buster

RUN pip install pipenv

COPY ./src /opt/app/src
COPY Pipfile /opt/app/
COPY Pipfile.lock /opt/app/

WORKDIR /opt/app/
ENV PYTHONUNBUFFERED=1

RUN pipenv install --deploy
WORKDIR /opt/app/src

CMD ["pipenv", "run", "python", "main.py"]
