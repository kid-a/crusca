##------------------------------------------------------------------------------
## tests.py
## 
## Unit tests for pywordcloud
##------------------------------------------------------------------------------

##------------------------------------------------------------------------------
## local imports
##------------------------------------------------------------------------------
from registry import Registry as Registry
from pywordcloud import Request as Request

##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
import glob
import unittest

##------------------------------------------------------------------------------
## class PropyleneTest
##------------------------------------------------------------------------------
class PyWordCloudTest(unittest.TestCase):
    
    def test_registry_insert (self):
        reg = Registry ()
        for i in range (10):
            request = Request ()
            request._value = "foo" + str (i)
            print request._value
            request_id = reg.register (request)
            self.assertEqual (request._value, reg[request_id]._value)
##
##------------------------------------------------------------------------------
##  Main
##------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
