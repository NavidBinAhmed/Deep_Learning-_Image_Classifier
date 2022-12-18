FROM python:3.9

RUN mkdir/ImagePrediction
WORKDIR /ImagePrediction

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE $PORT

CMD flask run --host=0.0.0.0 --port=5000