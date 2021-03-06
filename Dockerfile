FROM python:3.10-buster

RUN pip install pipenv

COPY ./src /opt/app/
COPY Pipfile /opt/app/
COPY Pipfile.lock /opt/app/

WORKDIR /opt/app/
ENV PYTHONUNBUFFERED=1

RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
