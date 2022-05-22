# API developed using FastAPI🚀 Framework (Python🐍)

### Basic CRUD API
DB used is sqlite 🗄️

**API response time is in second(s)**

API documentation 
=================
[API Documentation is at 'http://localhost:5000/docs'](http://localhost:5000/docs)

---

**[FastAPI Documentation](https://fastapi.tiangolo.com)**

**[FastAPI Source Code](https://github.com/tiangolo/fastapi)**

---

## Requirements

**This guide is written based on windows environment.**
Python 3.6+


## Installation

Firstly create a virtualenv for isolated python environment
**[Installing virtualenv](https://github.com/pypa/virtualenv)**

Activate the virtualenv & install the requirement. 

<div class="termy">

```console
$ pip install virtualenv # installing virtualenv

$ virtualenv venv # to create virtualenv 

$ venv\Scripts\activate # to activate venv

(venv)$ pip install -r req.txt # install the required module into the env 

(venv)$ deactivate # to deactivate virtualenv

---> 100%
```

</div>

## Example

### Run it

Run the server with:

Double-clicking the run.bat file. 

**OR** 

Using the cmd to run the API

<div class="termy">

```console
$ uvicorn run:app --reload

INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn run:app --reload</code>...</summary>

The command `uvicorn run:app` refers to:

* `run`: the file `run.py` (the Python "module").
* `app`: the object created inside of `run.py` with the line `app = create_app()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

### Check it

Open your browser at <a href="localhost:5000" class="external-link" target="_blank">localhost:5000</a>.

You will see the JSON response as:

```JSON
"Hello FastAPI!"
```

### Interactive API docs

Now go to <a href="http://127.0.0.1:5000/docs" class="external-link" target="_blank">http://127.0.0.1:5000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs

And now, go to <a href="http://127.0.0.1:5000/redoc" class="external-link" target="_blank">http://127.0.0.1:5000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### Interactive API docs upgrade

Now go to <a href="http://127.0.0.1:5000/docs" class="external-link" target="_blank">http://127.0.0.1:5000/docs</a>.

* The interactive API documentation will be automatically updated, including the new body:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

* Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

* Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

For a more complete example including more features, see the <a href="https://fastapi.tiangolo.com/tutorial/">Tutorial - User Guide</a>.

**Spoiler alert**: the tutorial - user guide includes:

* Declaration of **parameters** from other different places as: **headers**, **cookies**, **form fields** and **files**.
* How to set **validation constraints** as `maximum_length` or `regex`.
* A very powerful and easy to use **<abbr title="also known as components, resources, providers, services, injectables">Dependency Injection</abbr>** system.
* Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** auth.
* More advanced (but equally easy) techniques for declaring **deeply nested JSON models** (thanks to Pydantic).
* **GraphQL** integration with <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> and other libraries.
* Many extra features (thanks to Starlette) as:
    * **WebSockets**
    * extremely easy tests based on `requests` and `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...and more.

## Performance

Independent TechEmpower benchmarks show **FastAPI** applications running under Uvicorn as <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">one of the fastest Python frameworks available</a>, only below Starlette and Uvicorn themselves (used internally by FastAPI). (*)

To understand more about it, see the section <a href="https://fastapi.tiangolo.com/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Optional Dependencies

Used by Pydantic:

* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - for faster JSON <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>.
* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> - for email validation.

Used by Starlette:

* <a href="https://requests.readthedocs.io" target="_blank"><code>requests</code></a> - Required if you want to use the `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Required if you want to use the default template configuration.
* <a href="https://andrew-d.github.io/python-multipart/" target="_blank"><code>python-multipart</code></a> - Required if you want to support form <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, with `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Required for `SessionMiddleware` support.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Required for Starlette's `SchemaGenerator` support (you probably don't need it with FastAPI).
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Required if you want to use `UJSONResponse`.

Used by FastAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - for the server that loads and serves your application.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Required if you want to use `ORJSONResponse`.

You can install all of these with `pip install "fastapi[all]"`.