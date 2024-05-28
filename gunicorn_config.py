from os import getenv
from dotenv import load_dotenv

load_dotenv()

workers = int(getenv("GUNICORN_PROCESSES", "2"))
threads = int(getenv("GUNICORN_THREADS", "4"))
bind = getenv("GUNICORN_BIND", "0.0.0.0:8000")

forwarded_allow_ips = "*"

# secure_scheme_headers = {"X-Forwarded-Proto": "https"}
