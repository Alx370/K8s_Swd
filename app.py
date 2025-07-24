# Importa Flask per creare l'applicazione web e jsonify per restituire risposte JSON
from flask import Flask, jsonify 
# Importa CORS per gestire le richieste cross-origin
from flask_cors import CORS

# Crea un'istanza dell'applicazione Flask
app = Flask(__name__)
# Abilita CORS su tutta l'applicazione per permettere richieste da domini diversi
CORS(app)

# Definisce un endpoint per la route principale "/"
@app.route('/')
def home():
    # Restituisce una risposta JSON con un messaggio
    return jsonify({"message": "DAJE ROMA DAJE!"})

# Verifica se il file viene eseguito direttamente (non importato)
if __name__ == '__main__':
    # Avvia il server Flask in modalità debug, accessibile da tutti gli IP sulla porta 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
