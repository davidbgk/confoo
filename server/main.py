import os
import json

import falcon
import livereload
import tinydb

# The database is a JSON file, easy debugging!
db = tinydb.TinyDB('db.json')
pretty_print = {'sort_keys': True, 'indent': 4}


def serve_static(req, resp):
    """Serve static files from the `client` directory."""
    file_name = req.path[1:]  # Remove first slash.
    # Fallback to `index.html`.
    if not file_name:
        file_name = 'index.html'
    file_path = 'client/{name}'.format(name=file_name)
    # Deal with the content type for the browser.
    if file_name.endswith('.css'):
        content_type = 'text/css'
    else:
        content_type = 'text/html'
    resp.set_header('Content-Type', content_type)
    try:
        # No need to `.close()` or `with` given that we pass
        # directly a stream.
        resp.stream = open(file_path, 'rb')
        resp.stream_len = os.path.getsize(file_path)
    except FileNotFoundError:  # NOQA: outdated linter.
        resp.status = falcon.HTTP_404


class Tweets:
    def on_get(self, req, resp):
        """Return all tweets or filtered by `username`."""
        username = req.get_param('username')
        if username:
            tweet = tinydb.Query()
            data = db.search(tweet.username == username)
        else:
            data = db.all()
        resp.body = json.dumps(data, **pretty_print)

    def on_post(self, req, resp):
        """Store the JSON encoded tweet."""
        resp.status = falcon.HTTP_201
        data = json.loads(req.stream.read().decode())
        db.insert(data)
        resp.body = json.dumps(data, **pretty_print)

    def on_delete(self, req, resp):
        """Delete all tweets in the database."""
        resp.status = falcon.HTTP_204
        db.purge()
        # A 204 does not need a body.

# Launch the `app` and serve it with livereload.
app = falcon.API()
app.add_route('/tweets', Tweets())
app.add_sink(serve_static)
server = livereload.Server(app)
server.serve()
