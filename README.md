
Installation
```bash
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt
```

# Install db
```bash
. venv/bin/activate
export FLASK_APP=run.py;

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
export FLASK_APP=run.py;

flask db migrate
flask db upgrade
```
