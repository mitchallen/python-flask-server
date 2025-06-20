python-flask-server
==

[![Ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/mitchallen)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/mitchallen)


## Usage

* Start Docker
* Open the project in VS Code
* If you had just cloned this project, run:
```sh
poetry install
```

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

## Docker

### Build

Run these commands outside the dev container (in a regular terminal window)

```sh
docker build -t flask-svr .
```

### Docker Run

```sh
docker run -d -p 3000:3000 --restart always --name flask-server flask-svr
```

### Docker Clean

```sh
docker stop flask-server && docker rm flask-server && docker rmi flask-svr
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

## Quick Start (Makefile)

1. Install dependencies:

    make install

2. Run the server:

    make run

3. Run tests:

    make test

4. Build, run, or clean Docker images (outside a dev container):

    make docker-build
    make docker-run
    make docker-clean

5. Check if you are in a dev container:

    make in-devcontainer

For more options, run:

    make help

