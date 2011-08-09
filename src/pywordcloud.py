
class Request:
    """ Encapsulates a request."""
    
    def __init__ (self, *args, **kwargs):
        self._timestamp = None
        self._id = None ## ask the registry
        self._ip = None ## ip address
        ## other stuff


def count_words (u_string):
    t = u_string.split ()
    r = {}
    for token in t:
        try: r[token] = r[token] + 1
        except: r[token] = 1

    return r
    
# def tokenize (u_string):
#     return u_string.split(" ")
