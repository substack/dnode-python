# What DNode should look like (maybe) in python, on the server side

from dnode import DNode, DNode_decs

class For_DNode(object):
    def timesTen(self, n, reply):
        reply(n*10)
    def moo(self, reply):
        reply(100)

#ugly.
DNode(For_DNode()).listen(12321)

#Can this be done with a decorator? Say: 

@DNode_Decs.listen(12321)
class Also_For_DNode(object):
    def timesTen(self, n, reply):
        reply(n*10)
    def moo(self, reply):
        reply(100)

#Fuck, that's grody too.
