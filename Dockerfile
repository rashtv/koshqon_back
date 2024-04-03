FROM python:3.11.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /src

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y libpq-dev

#RUN python3 -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . /app
CMD ["python3", "src/manage.py", "runserver"]