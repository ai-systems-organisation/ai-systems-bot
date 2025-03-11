# FROM python:3.11-bullseye

# WORKDIR /app

# COPY ./ /app

# RUN python -m pip install -r requirements.txt

# RUN python -m pip install gunicorn

# CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0:8000", "main:app"]

FROM python:3.11-bullseye

WORKDIR /app/backend

COPY ./backend /app/backend

RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --no-cache-dir gunicorn

ENV PYTHONPATH="/app/backend"

CMD ["gunicorn", "-b", "0.0.0.0:8181", "main:app"]

