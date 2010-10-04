# This is currently NOT tests, but just notes on how the dNode protocol
# works. However, my next step is going to be making nose tests for making sure
# that mein enkoder/dekoder works proper. 

# Encoded messages generally have this form:

{
    "method": "string or integer";
    "arguments": ['array'];
    "callbacks": {"one o' dese"};
    "links": ['another array']
}
# Links is optional.

# This is what should be sent *first*:

{
    "method" : "methods",
    "arguments" : [ { "timesTen" : "[Function]", "moo" : "[Function]" } ],
    "callbacks" : { "0" : ["0","timesTen"], "1" : ["0","moo"] }
}

# (Arguments has an array with a js object. In python terms, this should be a dict where each function is replaced by "[function]".)

#callbacks is of the form id: [place in arguments, function key]

#Meanwhile, the original arguments are dumped into the "callback" field. For some reason this is hard for me to understand.

#Links can be ignored initially, but is used to deal with cyclic references.
