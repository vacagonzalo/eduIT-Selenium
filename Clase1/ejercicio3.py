import unittest
from selenium import webdriver

url = "https://www.felixcatinsurance.com/"


class FelixTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(url)
        self.assertIn('Felix', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
