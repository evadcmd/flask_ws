install dependencies

```
poetry install
```

run server

```
gunicorn -c gunicorn.conf.py flask_ws.main:app
```
