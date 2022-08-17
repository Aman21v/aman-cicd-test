import os
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
   name = os.environ.get("NAME", "World")
   return "Hello from A to {}!, Welcome to Test part 3333".format(name)
 
if __name__ == "__main__":
   app.run()
