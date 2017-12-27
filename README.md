
Installation
```bash
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt

# Install db
flask initdb
```

Run
```bash
. venv/bin/activate
python run.py
```

Migrations:
```bash
. venv/bin/activate
export FLASK_APP=app/__init__.py;
flask db migrate
flask db upgrade
```
