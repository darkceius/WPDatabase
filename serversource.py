#-- [Packages] --#
from flask import Flask, request, jsonify
import os
import json

#-- [DB Handler] --#
app = Flask(__name__)

def SaveDB(newDB):
  with open("database.json", "w") as f:
    json.dump(newDB, f)

def GetDB():
  with open("database.json", "r") as f:
    users = json.load(f)
  return users

@app.route('/', methods=['POST'])
def main():
    content = request.json

    if not 'secret' in content:
      return jsonify({"error":"Secret key is required.", "message":"ERROR"})

    if not content['secret'] == os.getenv("secret"):
      return jsonify({"error":"Invalid key.", "message":"ERROR"})
    

    if content['type'] == "ping":
      return jsonify({"message":"Pong!"})
    elif content['type'] == "stores":
      db = GetDB()
      return json.dumps(db)
    elif content['type'] == "addkey":
      if not 'data' in content:
        return jsonify({"error":"Data is required.", "message":"ERROR"})
      if not 'name' in content['data']:
        return jsonify({"error":"Name inside data is required.", "message":"ERROR"})
      if not 'value' in content['data']:
        return jsonify({"error":"Value inside data is required.", "message":"ERROR"})

      db = GetDB()
      data = content['data']

      db[data['name']] = data['value']
      SaveDB(db)
      return jsonify({"message":data['value']})
    elif content['type'] == "checkSecret":
      if not 'data' in content:
        return jsonify({"error":"Data is required.", "message":"ERROR"})
      if not 'value' in content['data']:
        return jsonify({"error":"Value inside data is required.", "message":"ERROR"})
      return jsonify({"message":content['data']['value']==os.getenv("secret")})

    elif content['type'] == "keyexists":
      if not 'data' in content:
        return jsonify({"error":"Data is required.", "message":"ERROR"})
      if not 'name' in content['data']:
        return jsonify({"error":"Name inside data is required.", "message":"ERROR"})

      db = GetDB()
      data = content['data']

      return jsonify({"message":data['name'] in db})
    elif content['type'] == "getkey":
      if not 'data' in content:
        return jsonify({"error":"Data is required.", "message":"ERROR"})
      if not 'name' in content['data']:
        return jsonify({"error":"Name inside data is required.", "message":"ERROR"})

      db = GetDB()
      data = content['data']

      if not data['name'] in db:
        return jsonify({"error":"Key doesn't exist.", "message":"ERROR"})

      return jsonify({"message":db[data['name']]})
    elif content['type'] == "removekey":
      if not 'data' in content:
        return jsonify({"error":"Data is required.", "message":"ERROR"})
      if not 'name' in content['data']:
        return jsonify({"error":"Name inside data is required.", "message":"ERROR"})

      db = GetDB()
      data = content['data']

      if not data['name'] in db:
        return jsonify({"error":"Key doesn't exist.", "message":"ERROR"})

      db.pop(data['name'])
      SaveDB(db)
      return jsonify({"message":"OK"})
    else:
      return jsonify({"error":"Unknown type.", "message":"ERROR"})
    

#-- [Running Server] --#
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
