from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route("/")
def hello():
    # redis = Redis(
    #     host= 'redis-master',
    #     port= '6379',
    #     password= 'yFZSNGR7zq')
    # redis.set('mykey', 'Hello from Python!')
    # value = redis.get('mykey') 
    # print("value from redis is ", value)
    return "Kubernetes on vSphere! #tanzu #vmware @KobiShamama @OdedShopen @INPRocks!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
