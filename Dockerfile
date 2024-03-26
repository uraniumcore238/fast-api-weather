FROM python:3.11-bookworm

WORKDIR /app

RUN apt-get update  \
   && rm -rf /var/lib/apt/lists/

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

COPY . /app
COPY requirements.txt /app

CMD ["python", "main.py"]