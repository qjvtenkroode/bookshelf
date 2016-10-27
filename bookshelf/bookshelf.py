import cherrypy
import os

import qkroode.authentication
import services.booksservices

if __name__ == '__main__':
    cherrypy.tree.mount(
        None, '/', {
            '/': {
                'request.dispatch': cherrypy.dispatch.Dispatcher(),
                'tools.auth_basic.on': True,
                'tools.auth_basic.realm': 'localhost',
                'tools.auth_basic.checkpassword': qkroode.authentication.validate_user,
                'tools.staticdir.on' : True,
                'tools.staticdir.dir' : os.getcwd() + '/catalog',
                'tools.staticdir.index' : 'catalog.html'
            }
        }
    )
    cherrypy.tree.mount(
        services.booksservices.BooksServices(), '/api/books', {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.auth_basic.on': True,
                'tools.auth_basic.realm': 'localhost',
                'tools.auth_basic.checkpassword': qkroode.authentication.validate_user
            }
        }
    )
    cherrypy.config.update({'engine.autoreload.on': True})

    cherrypy.engine.start()
    cherrypy.engine.block()
