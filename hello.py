def app(environ, start_response):
    data = environ['wsgi.input'].read()

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ('Content-Length', str(len(data))),
    ])

    return iter([data])