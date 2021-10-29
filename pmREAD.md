# Documentation for the pythonmodule.py file.
------------------------------------------
# Adding the module in your workspace:

Create a new file named WPDatabase.py then change the code inside the file to [this](https://raw.githubusercontent.com/a-a-a-a-a-a-a-a-a-a-a/WPDatabase/main/pythonmodule.py)

-----------------
# Using the module:

At the start of your code put this:
```py
from WPDatabase import wpdatabase
```

### Logging in with the token and secret key:

```py
my_database = wpdatabase(db_url = "[YOUR DATABASE URL]", secret_key = "[YOUR SECRET KEY]")
```

## Functions:

### ping()

```py
my_database.ping()
```
Returns string ("Pong!")

### getStores()
```py
my_database.getStores()
```
Returns a dict ({'key':'value'})

### addKey(name, value)
```py
my_database.addKey("name", "value")
```
Returns the a string (`The value`)

### checkSecret(value)
```py
my_database.checkSecret("asdsadasd")
```
Returns a boolean (True, False)

### keyExists(name)
```py
my_database.keyExists("name")
```
Returns a boolean (True, False)

### getKey(name)
```py
value = my_database.getKey("name")
```
Returns a string (`The value`)

### removeKey(name)
```py
my_database.removeKey("name")
```
Returns a string ("OK")

---
## Errors

### InvalidKey
Raises when you enter a invalid key inside the login function.

### UnknownError
Raises when an error occurred while calling a function (from webpage)

#### DatabaseError
Raises when an error has occurred inside the flask server.

