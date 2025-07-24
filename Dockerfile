# Utilizza l'immagine base python:3.11-slim per un ambiente leggero e aggiornato.
FROM python:3.11-slim

# Imposta la directory di lavoro su /app all'interno del container.
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro.
COPY requirements.txt .

# Installa le dipendenze Python specificate in requirements.txt senza salvare la cache.
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutti i file e le cartelle dal contesto di build nella directory di lavoro del container.
COPY . .

# Espone la porta 5000 per consentire l'accesso all'applicazione.
EXPOSE 5000

# Definisce il comando di default per avviare l'applicazione Python (app.py).
CMD ["python", "app.py"]
