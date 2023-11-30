from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def index():
    return "Welcome to my Flask App"


# if __name__ == "__main__":
#     # Dev only: run "python main.py" and open http://localhost:8080
#     app.run(host="localhost", port=8080, debug=True)
