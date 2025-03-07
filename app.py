from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/stream": {"origins": "*"}})  # Allow all origins for "/stream"

@app.route("/stream")
def stream():
    url = request.args.get("url")
    if not url:
        return "Missing URL", 400

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers, stream=True)
        response = Response(r.iter_content(chunk_size=1024), content_type=r.headers["Content-Type"])
        response.headers["Access-Control-Allow-Origin"] = "*"  # Allow cross-origin access
        return response
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

