from dnode import _conn_args as args
from dnode import DNodeError
#import nose
import nose.tools as nt

fxn = (lambda x: x+1)

def test_port_only():
    nt.eq_(args(1234), ('localhost', 1234, None))

def test_port_and_host():
    nt.eq_(args('jesusabdullah.net', 1234), ('jesusabdullah.net', 1234, None))

def test_port_and_fxn():
    nt.eq_(args(1234, fxn), ('localhost', 1234, fxn))

def test_port_fxn_and_host():
    nt.eq_(args('jesusabdullah.net', 1234, fxn), ('jesusabdullah.net', 1234, fxn))

@nt.raises(DNodeError)
def test_no_port():
    args('jesusabdullah.net', fxn)
