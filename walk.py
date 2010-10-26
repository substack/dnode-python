# Walk does some of the things that js-traverse does.

import types

class Walk(object):
    def __init__(self, cls, obj):
        self.path = []
        #Will probably have to do an obj --> dict transformation 
        #somewhere in here
        self.obj = obj

    def walk(self, cb):
        node = _Node({ 'value': self.obj, 'path': self.path })
        cb(node)
        #in dnode-perl, we checked 

class _Node(object):
    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.path = kwargs['path']

# Basically, __getitem__ == __getattr__
class Thesaurus(dict):
    def __init__(self, obj):
        self.update(obj);
    
    def __getitem__(self, key):
        return self.setdefault(key, None)
    
    def __getattr__(self, key):
        return self.setdefault(key, None)
    
    def __setattr__(self, key, value):
        self[key] = value
