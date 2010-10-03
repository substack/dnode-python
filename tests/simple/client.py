# What DNode should look like in python, on the client side

from dnode import DNode, DNode_decs

# Std.
def once_connected(remote):
    remote.moo(lambda x: print x)
    remote.timesTen(10, lambda x: assert(x == 100))

DNode().connect(12321, once_connected)

# Or:

@DNode_decs.connect(12321)
def once_connected_again(remote):
    remote.moo(lambda x: print x)
    remote.timesTen(10, lambda x: assert(x == 100))
