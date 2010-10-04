# Walk does some of the things that js-traverse does.

import types

class Walk(object):
    def __init__(self, cls, obj):
        self.path = []
        #Will probably have to do an obj --> dict transformation 
        #somewhere in here
        self.obj = obj

    def walk(self, cb):
        node = _Node({'value': self.obj,
                      'path': self.path})
        cb(node)
        #in dnode-perl, we checked 

class _Node(object):
    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.path = kwargs['path']

# Basically, __getitem__ == __getattr__
# http://modzer0.cs.uaf.edu/~substack/snippets/AttrDefaultDict.py
# may be helpful.
class Thesaurus(dic):
    pass
