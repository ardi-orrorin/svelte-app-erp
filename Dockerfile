FROM python:latest

WORKDIR /app/fastapi/

COPY ./fastapi/ /app/fastapi/
COPY ./piplist.txt /app/fastapi/

RUN pip install -r piplist.txt

CMD gunicorn --bind 0.0.0.0:8000 main:app --worker-class uvicorn.workers.UvicornWorker

#CMD uvicorn main:app --reload --host 0.0.0.0 --port 8080 --workers 10