# Full stack blockchain app.

# Pipenv

This project uses pipenv to manage the virtual environment.
If you do not have pipenv installed then you can find the installation instructions here:

```
https://pypi.org/project/pipenv/
```

To install the dependencies launch the terminal, change to the project root and type the following command: 

```python
pipenv install -r requirements.txt
```

Which will get the dependencies into your local environment.

# Invoke Tasks:

To run all the tests launch terminal, change directory to the project root
and input the following:

```python
inv run-all-tests
```

# Setup application from container.

If you have docker and docker compose already installed then you may omit the previous pipenv
installation instructions and just build the app in a container. To do so, launch the terminal
change to the project root and input the following:

```
docker-compose up
``` 

# More to come...