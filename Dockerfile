FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Nginx 설치 추가
RUN apt-get update && apt-get install -y nginx

# Nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Entrypoint: Nginx & Uvicorn 동시에 구동
CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8000

# docker build -t my-backend .
# docker run -d -p 8000:8000 my-backend --name my-backend