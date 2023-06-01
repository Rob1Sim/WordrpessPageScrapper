    FROM python:3.10-alpine3.18
    LABEL authors="Robin Simonneau"
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    EXPOSE 5000
    CMD ["python", "app.py"]
    ENV CONFIG_FILE=/app/scrapper/.env
    VOLUME /app/scrapper/templates
