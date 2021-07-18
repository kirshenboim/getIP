Who am I ?
==================

A Flask web app that display the visitor IP: **whoami**.

Use it now
----------

```sh
# Install requirements
$ pip install -r app/requirements.txt

# If you want the debug mode:
$ export FLASK_DEBUG=1

# Change settings in app/app.py (ex: SERVER_NAME)
$ vim app/app.py 
> app.config['DEBUG'] = True
> app.config['SERVER_NAME'] = "www.myserver.com"

# Run it:
$ FLASK_APP=app/app.py python3 -m flask run
 * Serving Flask app "app"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 129-590-285
```

Now point your browser at http://127.0.0.1:5000

If you want to change the host and port Flask will bound to, just run:

```sh
$ FLASK_APP=app/app.py python3 -m flask run --host=0.0.0.0 --port=6000
 * Serving Flask app "app"
 * Forcing debug mode on
 * Running on http://0.0.0.0:6000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 129-590-285
```

### Docker
**whoami** can easily be dockerized and is shipped with a ``Dockerfile``.

By default, the container will expose port 5000, so change this within the ``Dockerfile`` if necessary. When ready, simply use the ``Dockerfile`` to build the image.

```sh
cd app
docker build -t whoami .
```
This will create the Docker image.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 80 of the host to port 5000 of the container:

```sh
docker run -d -p 5000:5000 whoami 
```

Now point your browser at http://127.0.0.1/