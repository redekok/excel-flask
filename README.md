## Installation
The app is a python Flask app that has support for running in Docker. We recommend installing Docker on your system.

You can download a Docker image, or generate one yourself with `docker-compose build`

If you want to run the app locally in debug and reload-on-change mode, please use `docker-compose up`.

### Using pipenv in development
For development and testing please use [`pipenv`](https://pypi.org/project/pipenv/). Install and setup with the following commands:
```
pip3 install pipenv
pipenv install --dev
```
The `dev` flag is used to install development dependencies as well (like `pytest`).

You can now test your local changes by running `pytest`. You can use the shortcut:
```
pipenv run test
```

#### When the Pipfile changes
You can update your local dependencies when the Pipfile.lock was updated upstream by using
```
pipenv install --dev --ignore-pipfile
```

When you update the Pipfile manually please relock and install new dependencies by simply
```
pipenv install --dev
```


## Contact

Do you have any questions on the above? Don't bother to contact us!

* Roos ([https://github.com/redekok](https://github.com/redekok))
