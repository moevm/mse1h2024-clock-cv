FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt
RUN apt-get update && apt-get install abiword -y && apt-get install -y ca-certificates

COPY /clockcv /app/clockcv

CMD ["python", "-m", "clockcv.app"]
