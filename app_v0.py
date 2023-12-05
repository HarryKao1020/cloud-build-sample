from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def helloworld():
    return "Hello world"

@app.route('/')
def index():
    return "welcome line bot"

# if __name__ == "__main__":
#     # Dev only: run "python main.py" and open http://localhost:8080
#     app.run(host="0.0.0.0", port=8080, debug=True)
