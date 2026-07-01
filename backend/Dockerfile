FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --timeout 120 --retries 10 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY main.py /app/main.py

ENV APP_NAME=k8s-cloud-native-demo
ENV APP_ENV=docker
ENV APP_VERSION=v1
ENV LOG_LEVEL=info
ENV SECRET_TOKEN=docker-token
ENV PORT=8000

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
