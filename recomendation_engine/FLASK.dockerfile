FROM python:3.9-slim-bullseye
RUN echo 'y' | apt-get update
RUN echo 'y' | apt upgrade

WORKDIR /tmp
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./recomendation_engine.py ./recomendation_engine.py

CMD flask --app recomendation_engine run --host=0.0.0.0