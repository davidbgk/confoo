# Confoo - Small libs, loosely joined.

This repository contains an example of what can be achieved
from user to data through the browser with as few
dependencies as possible. It's useful for proof of concepts
and teaching the whole client-server roundtrip but it's
easy to switch components and to scale when it becomes
necessary.

It's highly opinionated:

- no package.json
- no requirements.txt
- minimal magic
- easy debugging
- fast testing
- integrated documentation
- limit lines to ~60 chars

The code will be presented for Confoo and I'll detail all
these points here after the conference.

A summary of the conference in French can be found here:
https://larlet.fr/david/blog/2016/minimalisme-esthetique/


### Run the server

    $ ./app.pex server/main.py

It will open your default browser, please note that only
a very recent version of Firefox will be able to run the
tests and use CSS variables natively.

### Run tests with silk

You'll have to install [Silk](https://github.com/matryer/silk)
or [download it](https://github.com/matryer/silk/releases).
And then:

    $ silk -silk.url=http://127.0.0.1:5500 README.md
    // => PASS


## Documentation

The documentation is tested using Silk to ensure that it's
always synchronized with the code.

# Tweets

## `DELETE /tweets`

Whenever you want you can erase all your previous tweets and
start with a fresh database. Note that it uses TinyDB so you
can always browse the JSON file to explore your data.

## `POST /tweets`

Let's create a new tweet using a JSON content type.

* `Content-Type`: `"application/json"`
* `Accept`: `"application/json"`

A tweet is composed of a `username` and a `content`:

```
{
    "username": "davidbgk",
    "content": "This is my last tweet."
}
```

===

### Response

It returns the tweet within the body with the appropriated
status code for a creation.

* `Status`: `201`
* `Content-Type`: `"application/json; charset=utf-8"`

We don't need to use ids at this point but your mileage may
vary, feel free to adapt:

```
{
    "content": "This is my last tweet.",
    "username": "davidbgk"
}
```

## `POST /tweets`

Now let's add a second tweet to test filtering.

* `Content-Type`: `"application/json"`
* `Accept`: `"application/json"`

```
{
    "username": "confooca",
    "content": "And now a talk from @davidbgk."
}
```

===

### Response

You can explore the response through `Data` attributes too:

* `Status`: `201`
* `Data.username`: `"confooca"`


## `GET /tweets`

Retrieve a list of all tweets.

===

### Response

The list is pretty-printed to ease debugging:

* `Status`: `200`
* `Content-Type`: `"application/json; charset=utf-8"`

```
[
    {
        "content": "This is my last tweet.",
        "username": "davidbgk"
    },
    {
        "content": "And now a talk from @davidbgk.",
        "username": "confooca"
    }
]
```

## `GET /tweets`

Retrieve a list of tweets from a given a `username` GET
parameter.

* `?username=davidbgk`

===

### Response

The response is still a list, filtered with the only tweet
from `davidbgk`:

* `Status`: `200`
* `Content-Type`: `"application/json; charset=utf-8"`

```
[
    {
        "content": "This is my last tweet.",
        "username": "davidbgk"
    }
]
```

## `DELETE /tweets`

Delete all tweets.

===

### Response

A deletion returns the appropriated status code:

* `Status`: `204`


# What’s next?

The code is not perfect and that's a feature, try the
mini-stack and adapt it to your own needs, some suggestions:

- add a new API endpoint
- refactor the logic for AJAX requests
- livereload silk tests
- add routes for filtering when you click a username
- make the refresh delay a parameter of the tag
- fix JS tests for Chromium
- improve mocha testing
- remove the server/requirements.txt file once tested

No need to propose a pull-request for that (remember that
I’m a starter ;-)), just enjoy!
