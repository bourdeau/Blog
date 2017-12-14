

Installation
```bash
python3 -m venv venv
. venv/bin/activate

pip instal Flask-SQLAlchemy
pip install pymysql
```

Run
```bash
. venv/bin/activate
python3 run.py
```

Migrations:
```bash
. venv/bin/activate
export FLASK_APP=blog/__init__.py;
flask db migrate
flask db upgrade
```
