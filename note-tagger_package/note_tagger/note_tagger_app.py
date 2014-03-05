#! /usr/bin/env python

import re
# import numpy
# import nltk

# from note_tagger_db import tagDB

# DB = tagDB()


def resolve_path(path):
    urls = [(r'^$', main_page),
            (r'^processnote$', note_tagger)]
    matchpath = path.lstrip('/')
    for regexp, func in urls:
        match = re.match(regexp, matchpath)
        if match is None:
            continue
        args = match.groups([])
        return func, args
    # we get here if no url matches
    raise NameError


def submit():
    pass


def main_page():
    with open('templates/note-tagger.html', 'r') as infile:
        return infile.read()


def note_tagger():
    return "Success"


def application(environ, start_response):
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body]

    # Example for getting post request
    # from paste.request import parse_formvars

    # fields = parse_formvars(environ)
    # if environ['REQUEST_METHOD'] == 'POST':
    #     start_response('200 OK', [('content-type', 'text/html')])
    #     return ['Hello, ', fields['name'], '!']
    # else:
    #     start_response('200 OK', [('content-type', 'text/html')])
    #     return ['<form method="POST">Name: <input type="text" '
    #             'name="name"><input type="submit"></form>']
    #
    ##############
#from webob import Request

# class Capitalizer(object):
#     def __init__(self, app):
#         self.app = app
#     def __call__(self, environ, start_response):
#         req = Request(environ)
#         resp = req.get_response(self.app)
#         resp.body = resp.body.upper()
#         return resp(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()


# def resolve_path(path):
#     urls = [(r'^$', note_tagger)]
    # urls = [(r'^$', note-tagger),
    #         (r'^book/(id[\d]+)$', book)]
    #
# def book(book_id):
#     page = """
#     <h1>{title}</h1>
#     <table>
#         <tr><th>Author</th><td>{author}</td></tr>
#         <tr><th>Publisher</th><td>{publisher}</td></tr>
#         <tr><th>ISBN</th><td>{isbn}</td></tr>
#     </table>
#     <a href="/">Back to the list</a>
#     """
#     book = DB.title_info(book_id)
#     if book is None:
#         raise NameError
#     return page.format(**book)
