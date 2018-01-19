My Blog
===============

## Installation
```bash
pipenv install
```

## Install db
```bash
pipenv shell
export FLASK_APP=run.py

flask init_db
```

## Run
```bash
pipenv shell
export FLASK_APP=run.py
export FLASK_DEBUG=1

flask run
```

## Migrations:
```bash
pipenv shell
export FLASK_APP=run.py

flask db migrate
flask db upgrade
```
