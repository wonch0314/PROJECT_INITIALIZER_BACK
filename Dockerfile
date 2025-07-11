FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Entrypoint: Nginx & Uvicorn 동시에 구동
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t chanchan0314/my-back .
# docker login -u chanchan0314
# password 입력

# docker push chanchan0314/my-back:latest

# docker run -d -p 8000:80 --network my-network --name my-back chanchan0314/my-back:latest