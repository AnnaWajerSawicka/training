import unittest
import aws
class TestStringMethods(unittest.TestCase):

    def test_g(self):
        self.assertTrue(True)

    def test_f1(self):
     
        w=aws.f1(0)
        self.assertEqual(w,0)

    def test_f1_2(self):
        w=aws.f1(1)
        self.assertEqual(w,1)

    def test_f1_3(self):
        w=aws.f1(2) 
        self.assertEqual(w,4)

    def test_f1_4(self):
        w=aws.f1(2,1)
        self.assertEqual(w,5)

    def test_f1_5(self):
        w=aws.f1(2,3)
        self.assertEqual(w,7)

    def test_f2(self):
        w=aws.f2("ala")
        self.assertEqual(w,"a")





if __name__=='__main__':
     unittest.main()
