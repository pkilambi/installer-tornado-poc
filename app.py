#!/usr/bin/env python
import yaml
import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/install", InstallerHandler)
        ]
        tornado.web.Application.__init__(self, handlers)
        
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("installer_form.html")

class InstallerHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.request.arguments
        fobj = open('setup.yaml', 'w')
        yaml.dump(data, fobj, default_flow_style=False)
        self.finish("setup.yaml generated with user input")

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    try:
        main()
    except:
        pass
