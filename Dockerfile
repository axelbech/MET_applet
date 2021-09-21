FROM python:3.8.5-slim-buster

RUN mkdir -p /home/pi/raspberry-sw
WORKDIR /home/pi/raspberry-sw

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

CMD ["python3", "./met_test.py" ]