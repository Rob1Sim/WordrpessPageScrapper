#!/bin/sh

LOG_FILE="/app/logs/server.log"

# Fonction pour démarrer le script Python
start_script() {
    echo "Démarrage du script Python..."
    python app.py >> "$LOG_FILE" 2>&1 &
    APP_PID=$!
    echo "Processus Python démarré. PID : $APP_PID"
}

# Fonction pour arrêter le script Python
stop_script() {
    echo "Arrêt du script Python..."
    kill $APP_PID
    wait $APP_PID
    echo "Processus Python arrêté."
}

# Vérification de l'heure de redémarrage
check_restart_time() {
    restart_hour="22"
    restart_minute="00"

    current_hour=$(date +%H)
    current_minute=$(date +%M)

    if [ "$current_hour" = "$restart_hour" ] && [ "$current_minute" = "$restart_minute" ]; then
        echo "Heure de redémarrage atteinte. Arrêt du script Python en cours..."
        stop_script
        start_script
    fi
}

# Démarrage initial du script Python
start_script

# Boucle infinie pour vérifier l'heure de redémarrage toutes les minutes
while true; do
    sleep 60
    check_restart_time
done
