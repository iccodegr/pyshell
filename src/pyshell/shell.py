import StringIO
import sys
import json
import mimetypes
import traceback
import os
from cherrypy import HTTPError
import cherrypy
from jedi import Script

from template import  TEMPLATE

import pkg_resources
try:
    VERSION = pkg_resources.get_distribution('pyshell').version
except pkg_resources.DistributionNotFound,e:
    VERSION = "0.10-dev"

STATIC_ROOT = '../frontend'

class ShellController(object):
    def __init__(self, production=True):
        if production:
            self.module = 'shell'
            self.production = production
        else:
            self.module = 'res/js/shell'
            self.production = production

        self.version = VERSION
        self.__resource_cache = {}
        self.__init_mapping()

    def __init_mapping(self):
        self.__keys = set()
        for p in dir(self):
            attr = getattr(self,p)
            if not callable(attr) and not hasattr(attr,'exposed'):
                self.__keys.add(p)

    def has_key(self,key):
        return key in self.__keys

    def keys(self):
        return list(self.__keys)

    def __getitem__(self, item):
        return getattr(self,item)

    def __open_resource(self, resource):
        import pkg_resources

        if self.production:
            if pkg_resources.resource_exists('pyshell.frontend', resource):
                return pkg_resources.resource_stream('pyshell.frontend',resource)
        else:
            respath = os.path.join(STATIC_ROOT,resource)
            if os.path.exists(respath):
                return open(respath,'r')

        raise HTTPError(404)


    def res(self, *args, **kw):
        resource = "/".join(args)

        mimetype, encoding = mimetypes.guess_type(resource)
        cherrypy.response.headers['Content-Type'] = mimetype
        cherrypy.response.headers['Cache-Control'] = "max-age=31556926"

        if resource in self.__resource_cache:
            return self.__resource_cache[resource]

        with self.__open_resource(resource) as f:
            data = f.read(-1)
            self.__resource_cache[resource]= data
            return data
    res.exposed = True

    def complete(self,column, line, script):
        column = int(column)
        line = int(line)

        completer = Script(script, line+1, column+1, '')
        completes = completer.complete()

        def transform(complete):
            return complete.word

        return json.dumps(map(transform, completes))
    complete.exposed = True

    def execute(self,script):
        io = StringIO.StringIO()
        oldErr = sys.stderr
        oldOut = sys.stdout

        sys.stderr = io
        sys.stdout = io

        try:
            compiled = compile(script,"<script>", "exec")
            exec compiled
        except:
            io.write(traceback.format_exc())

        sys.stderr = oldErr
        sys.stdout = oldOut

        return io.getvalue()
    execute.exposed = True

    def index(self,*args,**kw):
        print args, kw
        return TEMPLATE.format(**self)
    index.exposed = True


wsgi_app = cherrypy.Application(ShellController())

if __name__=="__main__":
    cherrypy.quickstart(ShellController(False))
