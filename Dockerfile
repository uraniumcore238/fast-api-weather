FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY weather /app/weather

CMD ["uvicorn", "weather.weather:app", "--host", "0.0.0.0"]