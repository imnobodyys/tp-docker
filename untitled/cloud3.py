from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

# Configuration MongoDB
MONGO_URI = "mongodb://mongo:27017/"
DB_NAME = "flask_db"

def get_mongo_client():
    """Crée une connexion MongoDB"""
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        # Vérifie la connexion
        client.admin.command('ping')
        print("Connexion MongoDB réussie!")
        return client
    except ConnectionFailure as e:
        print(f"Erreur de connexion MongoDB: {e}")
        return None

@app.route('/')
def hello_world():
    return '''
    <h1>Hello World avec MongoDB!</h1>
    <p>Bienvenue dans mon application Flask avec Docker Compose</p>
    <a href="/test-db">Tester la connexion à MongoDB</a>
    '''

@app.route('/test-db')
def test_db():
    """Route pour tester la connexion MongoDB"""
    client = get_mongo_client()

    if client is None:
        return jsonify({
            "status": "error",
            "message": "Impossible de se connecter à MongoDB"
        }), 500

    try:
        # Accéder à la base de données
        db = client[DB_NAME]

        # Insérer un document de test
        collection = db.test_collection
        test_doc = {
            "message": "Test de connexion réussi",
            "timestamp": "2026-01-11"
        }
        result = collection.insert_one(test_doc)

        # Compter les documents
        count = collection.count_documents({})

        return jsonify({
            "status": "success",
            "message": "Connexion MongoDB réussie!",
            "database": DB_NAME,
            "documents_count": count,
            "inserted_id": str(result.inserted_id)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erreur: {str(e)}"
        }), 500

    finally:
        client.close()

@app.route('/data')
def get_data():
    """Route pour récupérer les données de MongoDB"""
    client = get_mongo_client()

    if client is None:
        return jsonify({"error": "Connexion impossible"}), 500

    try:
        db = client[DB_NAME]
        collection = db.test_collection

        # Récupérer tous les documents
        documents = list(collection.find({}, {"_id": 0}))

        return jsonify({
            "status": "success",
            "count": len(documents),
            "data": documents
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        client.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)