from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok c'est bien"})

@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True)