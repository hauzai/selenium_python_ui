import unittest


def add(a, b):
    return a + b



class testadd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类方法setUp")

    def setUp(self):
        print("setup方法。。。。。。。。。")

    def test_add1(self):
        print("test_add1测试开始。。。。。。。。")
        self.assertEqual(add(1, 2), 3)

    @unittest.skipUnless(1 > 2,"跳过测试用例add2")
    def test_add2(self):
        print("test_add2测试开始。。。。。。。。")
        self.assertEqual(add("Hello", "World"), "HelloWorld")
    def tearDown(self):
        print("tearDown方法。。。。。。。")

    @classmethod
    def tearDownClass(cls):
        print("类方法teardown")

if __name__ == '__main__':
    unittest.main()