from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Hehe")
    return "Hello, Jenkins Multi-Stage Pipeline!"

if __name__ == "__main__":
    app.run(debug=True)