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
        self.routes = {}

    def route(self, routeUrl):
        def decorator(func):
            self.routes[routeUrl] = func
            return func
        return decorator

    def get(self, routeUrl):
        if routeUrl in self.routes.keys():
            return self.routes[routeUrl]()
        else:
            return 'ERROR - no such page'

    




# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
