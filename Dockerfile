FROM python:3.11

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run Alembic migrations before starting FastAPI
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
