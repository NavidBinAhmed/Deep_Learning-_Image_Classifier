FROM python:3.9

RUN mkdir/a2model_webapp
WORKDIR /2model_webapp

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE $PORT

CMD flask run --host=0.0.0.0 --port=5000
