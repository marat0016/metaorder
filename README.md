# Metaorder CRM

### Setup
- Make virtualenv - `python -m venv menv` win, `virtualenv --python=python3.4 menv` lin
- activate it - `cd menv/Scripts/ & activate.bat & cd ../..` win, `source menv/bin/activate` lin
- Install e.g. local deps - `pip install -r deps/local.txt`
- Migrate DB - `python apps/manage.py migrate`
- Run - `python apps/manage.py runserver`

### Project structure
- `deps` folder contain dependencies.
- `apps` standart Django apps folder.

### Requirements
- Python >= 3.4
- pip
- virtualenv
