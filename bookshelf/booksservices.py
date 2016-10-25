import cherrypy
import pymongo

import services

from bson.objectid import ObjectId


class BooksServices(services.Services):

    exposed = True

    db = None
    collection = None

    def __init__(self):
        self.db = pymongo.MongoClient('localhost', 27017).bookshelf
        self.collection = self.db.books

    @cherrypy.tools.json_out(handler=services.json_handler)
    def GET(self, id=None):
        if id is None:
            books = []
            for book in self.collection.find():
                books.append(book)
            return books
        elif self.get_id(id):
            return self.get_id(id)
        else:
            raise cherrypy.HTTPError(404, "Resource not found.")

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out(handler=services.json_handler)
    def POST(self):
        return self.get_id(self.collection.insert_one(cherrypy.request.json).inserted_id)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out(handler=services.json_handler)
    def PUT(self, id):
        if id is None:
            raise cherrypy.HTTPError(405, "Method not implemented.")
        self.collection.replace_one({'_id': ObjectId(id)}, cherrypy.request.json)
        return self.get_id(id)

    @cherrypy.tools.json_out(handler=services.json_handler)
    def DELETE(self, id):
        if id is None:
            raise cherrypy.HTTPError(405, "Method not implemented.")
        self.collection.delete_one({'_id': ObjectId(id)})
        return True
