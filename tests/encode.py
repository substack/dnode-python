from remote_class import Remote_Class
import nose.tools as nt
from conn import methods

def test_encode():
    #Will probably not be exactly the same, even as equivalent JSON.
    nt.eq_(methods(Remote_Class), '{"method" : "methods", "arguments" : [ { "timesTen" : "[Function]", "moo" : "[Function]" } ], "callbacks" : { "0" : ["0","timesTen"], "1" : ["0","moo"] } }')


