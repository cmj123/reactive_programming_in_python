import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world\n\nAwesome\n")

def make_app():
    routes = [
        (r"/", MainHandler)
    ]
    return tornado.web.Application(routes)

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
