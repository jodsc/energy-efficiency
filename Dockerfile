FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "energy_app.py" ]