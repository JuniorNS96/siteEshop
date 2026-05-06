FROM python:3.13

WORKDIR /app

# deps de produção
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# deps de dev
COPY pyproject.toml .
RUN pip install --no-cache-dir .[dev]  && pip show ruff


COPY app/ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]