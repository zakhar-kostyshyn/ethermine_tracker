FROM python:3.9-alpine

RUN mkdir tracker
WORKDIR /tracker
COPY requirements.txt ./

RUN apk update
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 -u tracker.py


