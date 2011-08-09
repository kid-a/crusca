""" 

registry.py
The registry of submitted requests. 
It is a Borg, all of its methods are synchronized. 

"""

class Registry:
    __requests = {}
    
    def __init__ (self):
        self.__dict__ = self.__requests

    def __getitem__ (self, id):
        return self.__requests[id]

    def __delitem__ (self, id):
        try: del self.dict[id]
        except: print "Warning. Tried to delete key %s which doesn't exist."

    def register (self, uRequest):
        ## generate a new request id, 
        id = len (self.__requests)
        uRequest._id = id
        self.__requests[id] = uRequest
        return id

    def keys (self):
        return self.__requests.keys ()

    def __repr__ (self):
        return str (self.__requests)
