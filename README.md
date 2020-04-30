### Iter Socketio Example

Install:
Make sure to use python3, since socket `threading` package depends on a feature added in 3.4
```
pipenv install --python /usr/local/bin/python3
```

Run:
```
pipenv shell
ITER_USERNAME=yourusername ITER_PASSWORD=yourpassword PYTHONWARNINGS="ignore:Unverified HTTPS request" python lib-socketio.py
```
