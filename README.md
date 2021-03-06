# WPDatabase
## A Roblox-To-Webpage database using python & flask
-------------

# How to setup a Flask webpage:

Requirements:
- Must have a [Replit](https://replit.com/~) account.
- Must be familiar with JSON & Python

--------------------

Step 1. Create and setup a Python [Repl](https://replit.com/~).

![image](https://user-images.githubusercontent.com/74603733/138714562-46a28540-c789-4d82-994c-21f6ca0f7471.png)


Step 2. Inserting files.

- After creating a Repl, put this code in `main.py`:
```py
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
```

Create a new file and name it `database.json`.

![image](https://user-images.githubusercontent.com/74603733/138715380-839f80a5-c29d-4d59-84e8-cdc546cd0c59.png)

![image](https://user-images.githubusercontent.com/74603733/138715425-2834411d-6ca4-4f4e-9a05-667947e54422.png)

![image](https://user-images.githubusercontent.com/74603733/138715482-afa85cc0-47ac-49de-a4cc-b83495c33624.png)

![image](https://user-images.githubusercontent.com/74603733/138715854-f6ae20a0-f342-43e7-8d22-eff7e17e0e20.png)

Now after you're done with the file creating proccess, lets get to the running & secret key part

-----------------------------------
Step 3. Secret Key

Press the 5th button on the left bar.

![image](https://user-images.githubusercontent.com/74603733/138716182-3ecd29cf-d3cd-4fb0-8be2-5bd244e3cd21.png)

Create a new key, name it `secret` and put something in. (Something safe or else someone can find your key and mess up your database.)

![image](https://user-images.githubusercontent.com/74603733/138716494-a964e52f-2317-44ee-b23b-6b127966255f.png)

Click on `Add a new secret`. Step 3 is done.

--------------------------
Step 4. Running the flask server

Tap this big green `Run` button 

![image](https://user-images.githubusercontent.com/74603733/138716970-29c07285-62c4-48f9-9f95-79d299ee965f.png)

In 1-2 minutes your `Run` button will turn gray and it should say `Stop`. That's a good sign.

Now let's copy the URL of your database.

![image](https://user-images.githubusercontent.com/74603733/138717522-89b3cf52-5ca4-482d-ac6f-23a412a1257d.png)

![image](https://user-images.githubusercontent.com/74603733/138717662-aaa1d98b-6393-4077-84d8-25fbffedcc6b.png)

I hid my URL for safety reason. Copy it and keep somewhere in a notepad so you don't lose it.

--------------------------
Step 5. The Roblox Module

[Click me to get redirected to the module](https://www.roblox.com/library/7833314427/WPDatabase)
- Get the model and place it in your studio place (If you don't know how to do this just search up a tutorial on how to do it.)

Place the module in the **ServerStorage**
You will need your **Database URL** and **secret key** for you to log-in the database.

Create a script in the **ServerScriptService** with the following code:

```lua
local WPD = require(game:GetService("ServerStorage")['WPDatabase'])
local DB = WPD:newDatabase({
	secret_key = "[PLACE YOUR SECRET KEY HERE]",
	http_link = "[PLACE THE DATABASE LINK HERE]"
})
```

Here comes the use of the **Database URL** and the **secret key**.

```py
secret_key = "my cool secret key",
http_link = "https://[your database url]"
```

If you've been putting correct things this entire time, it shouldn't error. 
Check the documentation inside the module. (from line 2 to 27)

How to create or edit a key:
```
DB:addKey("MyMessage", "Thanks for using my database module!")
```
