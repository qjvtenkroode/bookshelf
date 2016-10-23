import cherrypy

import booksservices

if __name__ == '__main__':
    cherrypy.tree.mount(
        booksservices.BooksService(), '/api/books', {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
            }
        }
    )
    cherrypy.config.update({'engine.autoreload.on': True})

    cherrypy.engine.start()
    cherrypy.engine.block()
