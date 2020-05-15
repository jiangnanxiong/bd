from selenium import webdriver
import unittest
import time


class Test_url(unittest.TestCase):
    def setUp(self) -> None:
        self.deriver=webdriver.Chrome()
        self.deriver.maximize_window()

    def test_url(self):
        self.deriver.get('https://www.baidu.com/')
        time.sleep(3)
        self.assertEqual(self.deriver.title,'百度一下，你就知道')

    def tearDown(self) -> None:
        self.deriver.quit()


if __name__ == '__main__':
    unittest.main()