<<<<<<< HEAD
FROM python:3.9

RUN mkdir/ImagePrediction
WORKDIR /ImagePrediction

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE $PORT

CMD flask run --host=0.0.0.0 --port=5000
=======
FROM python:3.9
COPY . /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT a2model_webapp:a2model_webapp
>>>>>>> ee69a47b2302526553b08abb12e4047d6b3e1ad2
