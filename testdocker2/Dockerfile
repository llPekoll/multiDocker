From python:3.7-stretch

COPY ./app /app

RUN apt update 
RUN apt install -y postgresql postgresql-contrib 
RUN pip3 install uvicorn fastapi[all]
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]