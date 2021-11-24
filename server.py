from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route("/")
def hello():
    redis = Redis(
        host= 'redis-master',
        port= '6379',
        password= 'KyyFmwDuc9')
    return "Kubernetes on vSphere! #tanzu #vmware @KobiShamama @OdedShopen @INPRocks!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=False)
