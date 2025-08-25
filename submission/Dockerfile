FROM python:3.11-slim

WORKDIR /app

COPY submission/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY submission/ .

# Start FastAPI dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]

