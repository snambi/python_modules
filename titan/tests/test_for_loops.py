from titan.loops import for_loops
import unittest

class Test_for_loops(unittest.TestCase):

    def test_for_loops( self ):
        a = [3,4,5,5,6,7,78,8]
        x = for_loops(a)
        
        self.assertEquals(x, a)
    

if __name__ == '__main__':
    unittest.main()    