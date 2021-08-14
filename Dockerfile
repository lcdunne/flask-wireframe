FROM python:3.9.6-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY wireframe .

EXPOSE 5000

CMD [ "python3", "run.py" ]