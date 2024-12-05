FROM python:3.9-slim-bullseye
RUN echo 'y' | apt-get update
RUN echo 'y' | apt upgrade
RUN echo 'y' | apt install wget

WORKDIR /tmp
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./model_generator.py ./model_generator.py
COPY ./entrypoint.sh ./entrypoint.sh

CMD [ "bash", "./entrypoint.sh" ]