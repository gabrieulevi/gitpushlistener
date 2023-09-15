from flask import Flask, request, jsonify
import subprocess, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
@app.route("/", methods=["POST"])
def triggerPull():
    data = request.get_json()
    
    repo_path = os.getenv("REPO_PATH")

    try:

        result = subprocess.run(["git", "pull"], cwd=repo_path, capture_output=True, text=True, check=True)
        
        print(result.stdout)

        return "pull into the main webserver", 200
    except subprocess.CalledProcessError as e:
        
        print("Git pull error:", e.stderr)
        return "Repo pull error", e.stderr, 500



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5066)