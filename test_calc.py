import unittest

class calc:

    def add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mul(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
class Exception:
    pass

class testCalc(unittest.TestCase):

    def setUp(self):
        print("Setting up the test")
        self.a = 10
        self.b = 5
    
    def test_add(self):
        print("Testing up")
        self.assertEqual(calc.add(self.a,self.b),15)
    
    def test_sub(self):
        print("Testing up")
        self.assertEqual(calc.sub(self.a,self.b),5,msg = "wrong input")
    
    def test_mul(self):
        print("perform Multiplication")
        self.assertRaises(Exception,calc.mul,self.a,self.b)   

    def tearDown(self):
        print("Cleaning the test suite ")
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()
