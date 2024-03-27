FROM python:3.11

WORKDIR /app
COPY clockcv-backend/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt
RUN apt-get update && apt-get install abiword -y && apt-get install -y ca-certificates
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*
COPY clockcv-backend/clockcv /app/clockcv

WORKDIR /app
CMD ["python", "-m", "clockcv.app"]