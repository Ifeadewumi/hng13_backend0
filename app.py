from flask import Flask, jsonify
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def me():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        data = response.json()
        fact = data.get("fact", "No fact available.")
    except Exception as e:
        fact = "Unable to fetch cat fact at this time."

    result = {
        "status": "success",
        "user": {
            "email": "agapereality@gmail.com",
            "name": "Ifeoluwa Adewumi",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
