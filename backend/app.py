# TODO: UPDATE THIS FILE FOR DEPLOYMENT
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os

app = Flask(__name__)

# We can comment this CORS config for the production because we are running the frontend and backend on the same server
# CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

frontend_folder = os.path.join(os.getcwd(),"..","frontend")
dist_folder = os.path.join(frontend_folder,"dist")
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# Handle CORS preflight requests (OPTIONS)
@app.route('/api/friends', methods=['OPTIONS'])
@app.route('/api/friends/<int:user_id>', methods=['OPTIONS'])
@cross_origin(origins="http://localhost:3000", headers=["Content-Type", "Authorization"])
def handle_options(user_id=None):
    return jsonify({'message': 'CORS preflight successful'}), 200
# Server static files from the "dist" folder under the "frontend" directory
@app.route("/",defaults={"filename":""})
@app.route("/<path:filename>")
def index(filename):
  if not filename:
    filename = "index.html"
  return send_from_directory(dist_folder,filename)

# api routes
import routes

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)