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
    urlMapping = {}
    def route(self, routeUrl):
        def decorator(func):
            def wrapper(*args, **kwargs):
                WebApp.urlMapping[routeUrl] = func(*args, **kwargs)
            return wrapper
        return decorator

    def get(self, routeUrl):
        def decorator2(func):
            def wrapper2(*args, **kwargs):
                if routeUrl in WebApp.urlMapping.keys():
                    return WebApp.urlMapping[routeUrl]
            return wrapper2
        return decorator2
    




# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
