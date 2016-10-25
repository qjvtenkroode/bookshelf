import cherrypy

import booksservices
import qkroode.authentication

if __name__ == '__main__':
    cherrypy.tree.mount(
        booksservices.BooksService(), '/api/books', {
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
