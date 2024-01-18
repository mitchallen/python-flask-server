python-flask-server
==

## Usage

* Start Docker
* Open the project in VS Code

* **Run this from within the VS Code terminal window:**

```sh
# poetry run flask run --port 3000
poetry run python -m server
```

Browse to:

* http://localhost:3000/
* http://localhost:3000/hello

* * *

## Run tests

* See: https://flask.palletsprojects.com/en/2.3.x/testing/

```sh
poetry run pytest
```

* * *

## Setup Notes

* Add .gitignore file for Python
* Create a Python + Poetry container

### init

```sh
poetry init
```

**Would you like to define your main dependencies interactively? (yes/no)** 

* Select `flask` as a dependency

**Would you like to define your development dependencies interactively? (yes/no)**

* Select `pytest` and `pytest-bdd` as dev dependencies

* Alternative way to add dev dependencies:

```sh
poetry add pytest pytest-bdd -D
```

