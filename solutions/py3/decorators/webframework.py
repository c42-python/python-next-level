'''
Create the scaffolding for a Flask-like framework.

>>> app = WebApp()
>>> @app.route("/")
... def index():
...     return 'Index Page'
...
>>> @app.route("/contact/")
... def contact():
...     return 'Contact Page'
...
>>> app.get("/")
'Index Page'
>>> app.get("/contact/")
'Contact Page'
>>> app.get("/no-such-page/")
'ERROR - no such page'


'''

# Write your code here:

class WebApp:
    def __init__(self):
        self.routes = dict()
    # This decorator breaks the mold of others you've seen so far,
    # because it doesn't actually modify the bare function in any way.
    # All we need to do is register the url in self.routes.
    def route(self, url):
        def decorator(func):
            self.routes[url] = func
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    # See how wrapper above just calls func, without doing anything
    # else?  That means we don't need a wrapper at all! So we can
    # abbreviate route() to just this:
    def route(self, url):
        def decorator(func):
            self.routes[url] = func
            return func
        return decorator
    def get(self, url):
        try:
            return self.routes[url]()
        except KeyError:
            return 'ERROR - no such page'
            

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
