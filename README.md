# Python Web App

This is a simple Python web application using Flask, with unit tests.

## Features
- Simple HTTP server with Flask
- `/` endpoint returning "Hello, World!"
- `/health` endpoint returning "OK"
- Unit tests using `unittest`
- JUnit XML test reporting

## Project Structure
```
python-web-app/
│── app.py
│── test_app.py
│── README.md
│── requirements.txt
```

## Installation
```sh
git clone https://github.com/your-repo/python-web-app.git
cd python-web-app
pip install -r requirements.txt
```

## If you add more packages in the future, you can update the requirements.txt file with:
```
pip freeze > requirements.txt
```

## Running the Application
```sh
python app.py
```

## Running Tests
```sh
python -m unittest test_app.py
```

For JUnit reports:
```sh
pytest --junitxml=test-results.xml
```
