import os
import json
import typing
import subprocess
from redis import Redis
from flask import Flask, request, jsonify

app = Flask(__name__)

r = Redis(host='redis', port=6379)

def construct(id: str, language: str, code: str) -> typing.Tuple[str, str]:
    cmd_ext = {
        "go": ("go run _.go", "go"),
        "c++": ("g++ _.cpp -o _ && ./_", "cpp"),
        "java": ("javac _.java && java _"),
        "python": ("python3 _.py", "py"),
        "javascript": ("node _.js", "js")
    }
    cmd, ext = cmd_ext.get(language)
    cmd = cmd.replace("_", id)
    file = f"{id}.{ext}"
    
    with open(file, 'w') as f:
        f.write(code)
    
    return cmd, file

@app.route("/", methods=["POST"])
def main():
    data = jsonify(request.json)
    id, language, code = data.id, data.language, data.code

    cmd, file = construct(id, language, code)
    
    output = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    r.set(id, json.dumps({
        "id": id,
        "language": language,
        "output": output,
    }), ex=3600)
    
    os.remove(file)
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)