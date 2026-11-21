from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello from Flask in Docker!</h1>
    <p>Built by Bhagyashri Jamadar, DevOps &amp; AWS</p>
    <p>Check <a href="/health">/health</a> for the health status.</p>
    """


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
