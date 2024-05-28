FROM python:3.10

WORKDIR /app/

COPY .env .
COPY requirements.txt .
COPY main.py .
COPY utils/ ./utils/
COPY gunicorn_config.py .

RUN python -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ ".venv/bin/gunicorn", "--config", "gunicorn_config.py", "-b", "0.0.0.0:8000", "main:app" ]