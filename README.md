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

## Deploy ed utilizzo con Kubernetes

1. Crea un Pod (opzionale, per test):
   ```sh
    kubectl apply -f pod.yaml --dry-run=client --validate=true #per testare prima
   kubectl apply -f pod.yaml
   ```

2. Crea un Deployment:
   ```sh
   kubectl apply -f deployment.yaml --dry-run=client --validate=true #per testare prima
   kubectl apply -f deployment.yaml
   ```

3. Crea un Service per esporre l'applicazione:
   ```sh
    kubectl apply -f service.yaml --dry-run=client --validate=true #per testare prima
   kubectl apply -f service.yaml
   ```

4. Controlla lo stato delle risorse:
   ```sh
   kubectl get pods
   kubectl get deployments
   kubectl get services
   ```

5. (Opzionale) Cancella le risorse:
   ```sh
   kubectl delete -f service.yaml
   kubectl delete -f deployment.yaml
   kubectl delete -f pod.yaml
   ```

6. (Opzionale) Visualizza i log di un pod:
   ```sh
   kubectl logs <nome-pod>
   ```

7. (Opzionale) Accedi a un pod in esecuzione:
   ```sh
   kubectl exec -it <nome-pod> -- /bin/bash
   ```

   8. Apri la porta del servizio per accedere all'applicazione:
   ```sh
   kubectl portforward svc/<nome> 5000:5000
   ```


## Struttura dei file

- `app.py`: Applicazione Flask principale
- `requirements.txt`: Dipendenze Python
- `Dockerfile`: Configurazione per il container Docker
- `pod.yaml`: Definizione di un Pod standalone (test)
- `deployment.yaml`: Definizione del Deployment Kubernetes
- `service.yaml`: Definizione del Service Kubernetes
- `README.md`: Questo file

## Note

L'applicazione è pronta per essere integrata in pipeline CI/CD e orchestrata tramite Kubernetes o altri orchestratori di container.