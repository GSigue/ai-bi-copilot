FROM python:3.12-slim

WORKDIR /app

# prevent .pyc files + buffer logs (production best practice)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# expose API port
EXPOSE 8000

# production-style startup
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]