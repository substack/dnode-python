from conn import Conn #parallels conn.js

#connexxion stuff
import eventlet
from eventlet.green import socket

import types

class DNodeError(Exception):
    pass

class DNode(object):
    def __init__(self, wrapped):
        #DNode({})
        pass

    def on(self):
        # Event-listening behavior
        pass

    def connect(self, *args, **kwargs):
        (host, port, block) = _conn_args(args, kwargs)
        pass

    def listen(self):
        (host, port, block) = _conn_args(args, kwargs)
        pass

# Sorts out arguments to connection, which get significant amounts of leeway 
# actually! The flexibility of DNode's arguments is surprising.
# In other news: Type checking in python sucks. 
# Fuck you if you say I shouldn't be doing it anyway.
def _conn_args(args, kwargs):
    #Host
    host = filter(lambda x: isinstance(x, types.StringType), args)
    if len(host) == 0:
        host = kwargs['host'] if kwargs.has_key('host') else 'localhost'
    else:
        (host, ) = host
    #Port
    port = filter(isinstance(x, types.IntType), args)
    if len(port) == 0:
        try:
            port = kwargs['port']
        except KeyError:
            print('No port specified.')
            raise DNodeError
    else:
        (port, ) = port
    # Block
    block = filter(lambda x: isinstance(x, types.FunctionType) 
                          or isinstance(x, types.BuiltinFunctionType), args)
    if len(block) == 0:
        block = kwargs['block'] if kwargs.has_key('block') else None
    else:
        (block, ) = block
    return (host, port, block)
