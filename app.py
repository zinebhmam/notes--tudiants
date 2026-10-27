
from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {"etudiant": "Amina", "note": 15.5},
    {"etudiant": "Youssef", "note": 12.0}
]

@app.route("/")
def accueil():
    return "Bienvenue dans l'application des notes !"

@app.route("/health")
def health():
    return jsonify(status="ok", version="1.0")

@app.route("/notes")
def get_notes():
    etudiant = request.args.get("etudiant")

    if etudiant:
        resultats = [
            n for n in notes
            if n["etudiant"].lower() == etudiant.lower()
        ]
    else:
        resultats = notes

    return jsonify(resultats)

if __name__ == "__main__":
    app.run(debug=True)
