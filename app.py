from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    print("Server running on port 8080...")
    app.run(host="0.0.0.0", port=8080)
