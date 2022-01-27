FROM alpine:3.14

RUN mkdir /src

WORKDIR /src

COPY script.py .

RUN apk update && apk add python3 && apk add zip

CMD python3 script.py
