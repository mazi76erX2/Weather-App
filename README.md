# Weather-App
Django App using the Weather API

## Usage

* Install and create virtualenv

```bash
python install virtualenv
virtualenv venv
```

* Activate virtualenv and install dependencies

```bash
for Linux and Mac:
source venv/bin/activate

for Windows
/venv/Scripts/activate

pip install -r requirements.txt
```

* Run Django on your local server.

```bash
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

## Testing

1. Before running tests, make sure you have installed the dependencies. (These are included in the requirements file)

```bash
pip install -r requirements.txt
```

2. Run a coverage tp check the test coverage

```bash
python manage.py test
```
