FROM python:3.10.6-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /var/myapp
RUN pip install --upgrade pip && \
    pip install poetry==1.2.2
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main
COPY main.py .
CMD uvicorn main:app --host=0.0.0.0
