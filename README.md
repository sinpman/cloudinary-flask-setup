# cloudinary-flask-setup
A sample webapp with cloudinary setup, that performs image upload into cloudinary.

## Steps

### Step-1: 
Install Python3 (virtualenv), and activate virtualenv

``` 
$ python3 -m venv venv
$ source venv/bin/activate
```

### Step-2: 
Install/Upgrade pip
```
$ pip install --upgrade pip
```

### Step-3:
Install all modules from requirements.txt
```
$ pip install -r requirements.txt
```

### Step-4
Create a cloudinary account [here](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/jvlzhlknt3io4e9naclh).

### Step-5
Set up a few environmental variables

```
$ export FLASK_APP=application.py
$ export FLASK_ENV=development
$ export CLOUDINARY_URL=cloudinary://<API-Key>:<API-Secret>@<Cloud-name>
```

Hint: You will find your cloudinary url in your cloudinary dashboard.

### Step-6
Run the flask application.

```
$ flask run --host=127.0.0.1 --port=8080
```
