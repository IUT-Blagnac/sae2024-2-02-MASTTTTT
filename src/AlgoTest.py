import unittest
from Algo import *

class AlgoTest(unittest.TestCase):
    
    def test_RLE(self):
        self.assertEqual(RLE("abc"), "1a1b1c")
        self.assertEqual(RLE("abbccc"), "1a2b3c")
        self.assertEqual(RLE("aaabaa"), "3a1b2a")
        self.assertEqual(RLE("aAa"), "1a1A1a")
        self.assertEqual(RLE("WWWWWWWWWWWWW"), "9W4W")
        self.assertEqual(RLE("WWWWWWWWWBWWWWWWWWBBBWWWBWWWWWWW"), "9W1B8W3B3W1B7W")

    def test_RLE_recursif(self):
        self.assertEqual(RLE_iterations("", 1), "")
        self.assertEqual(RLE_iterations("", 3), "")
         
        self.assertEqual(RLE_iterations("abc", 1), "1a1b1c")
        self.assertEqual(RLE_iterations("abbccc", 1), "1a2b3c")
        self.assertEqual(RLE_iterations("aaabaa", 1), "3a1b2a")
        self.assertEqual(RLE_iterations("aAa", 1), "1a1A1a")

        self.assertEqual((RLE_iterations("abc", 2)), "111a111b111c")
        self.assertEqual((RLE_iterations("abc", 3)), "311a311b311c")


    def test_unRLE(self):
        self.assertEqual(unRLE("1a1b1c"), "abc")
        self.assertEqual(unRLE("1a2b3c"), "abbccc")
        self.assertEqual(unRLE("3a1b2a"), "aaabaa")
        self.assertEqual(unRLE("1a1A1a"), "aAa")
        self.assertEqual(unRLE("9W4W"), "WWWWWWWWWWWWW")
        self.assertEqual(unRLE("9W1B8W3B3W1B7W"), "WWWWWWWWWBWWWWWWWWBBBWWWBWWWWWWW")

    def test_unRLE_recursif(self):
        self.assertEqual(unRLE_iterations("", 1), "")
        self.assertEqual(unRLE_iterations("", 3), "")
         
        self.assertEqual(unRLE_iterations("1a1b1c", 1), "abc")
        self.assertEqual(unRLE_iterations("1a2b3c", 1), "abbccc")
        self.assertEqual(unRLE_iterations("3a1b2a", 1), "aaabaa")
        self.assertEqual(unRLE_iterations("1a1A1a", 1), "aAa")

        self.assertEqual((unRLE_iterations("111a111b111c", 2)), "abc")
        self.assertEqual((unRLE_iterations("311a311b311c", 3)), "abc")
    

    def test_performance_RLE(self):
        import time
        input_str = "a" * 1000
        start_time = time.time()
        RLE(input_str)
        end_time = time.time()
        print(f"RLE performance test: {(end_time - start_time) * 1000:.2f} ms")

    def test_performance_unRLE(self):
        import time
        input_str = "9a1a" * 100
        start_time = time.time()
        unRLE(input_str)
        end_time = time.time()
        print(f"unRLE performance test: {(end_time - start_time) * 1000:.2f} ms")

if __name__ == '__main__':
    unittest.main()