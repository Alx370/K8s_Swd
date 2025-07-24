# K8s_Swd

Questa repository contiene una semplice applicazione web scritta in Python usando Flask, pensata per essere eseguita sia localmente che in ambiente containerizzato (Docker). L'app espone un endpoint che restituisce un messaggio JSON.

## Funzionalità

- Espone un endpoint `/` che restituisce `{"message": "DAJE ROMA DAJE!"}`
- Supporta richieste CORS
- Pronta per il deploy in ambienti containerizzati (es. Kubernetes)

## Requisiti

- Python 3.11+
- pip
- Docker (opzionale, per esecuzione containerizzata)

## Installazione ed esecuzione locale

1. Clona la repository:
   ```sh
   git clone https://github.com/Alx370/K8s_Swd
   cd K8s_Swd
   ```
2. Installa le dipendenze:
   ```sh
   pip install -r requirements.txt
   ```
3. Avvia l'applicazione:
   ```sh
   python app.py
   ```
4. Visita [http://localhost:5000](http://localhost:5000) per vedere la risposta JSON.

## Esecuzione con Docker

1. Costruisci l'immagine:
   ```sh
   docker build -t k8s_swd .
   ```
2. Avvia il container:
   ```sh
   docker run -p 5000:5000 k8s_swd
   ```
3. Visita [http://localhost:5000](http://localhost:5000)

## Struttura dei file

- `app.py`: Applicazione Flask principale
- `requirements.txt`: Dipendenze Python
- `Dockerfile`: Configurazione per il container Docker
- `README.md`: Questo file

## Note

L'applicazione è pronta per essere integrata in pipeline CI/CD e orchestrata tramite Kubernetes o altri orchestratori di container.