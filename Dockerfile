    FROM python:3.10-alpine3.18
    LABEL authors="Robin Simonneau"

    # Installation de cron
    RUN apk update && apk add --no-cache dcron
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    # Ajout de la tâche planifiée dans cron
    RUN echo "6       12       *       *       *       pkill -f app.py && sleep 5 && python app.py &" >> /etc/crontabs/root
    ENV CONFIG_FILE=/app/scrapper/.env
    EXPOSE 5000
    COPY entrypoint.sh /app/entrypoint.sh
    RUN chmod +x /app/entrypoint.sh
    ENTRYPOINT ["/app/entrypoint.sh"]
    VOLUME /app/scrapper/templates
