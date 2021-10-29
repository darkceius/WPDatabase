# The WPDatabase from Roblox in Python.

import json
import requests

class InvalidKey(Exception):
  pass

class UnknownError(Exception):
  pass

class DatabaseError(Exception):
  pass

class wpdatabase:
  def __init__(self, db_url:str , secret_key:str):
    self.key = secret_key
    self.dburl = db_url

  def ping(self):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"ping",
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if data['message'] == "ERROR":
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])
        

    return data['message']

  def getStores(self):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"stores",
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data
  
  def addKey(self, name, value):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"addkey",
      "data":{
        "name":name,
        "value":value,
      }
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data['message']
  
  def checkSecret(self, key):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"checkSecret",
      "data":{
        "value":key,
      }
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data['message']

  def keyExists(self, name):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"keyexists",
      "data":{
        "name":name,
      }
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data['message']
  def getKey(self, name):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"getkey",
      "data":{
        "name":name,
      }
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data['message']
    
  def removeKey(self, name):
    req = requests.post(self.dburl, json = {
      "secret":self.key,
      "type":"removekey",
      "data":{
        "name":name,
      }
    })

    try:
      req.json()
    except:
      raise DatabaseError("An internal server error occurred.")

    data = req.json()

    if "error" in data:
      if data['error'] == "Invalid key.":
        raise InvalidKey("The key is invalid.")
      else:
        raise UnknownError(data['error'])

    return data['message']



  
