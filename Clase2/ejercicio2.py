import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.easy.com.ar/"


class FelixTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.addCleanup(self.browser.quit)

    def testCompraCafetera(self):
        inputXpath = '//*[@placeholder="¡Hola! ¿Qué estás buscando?"]'
        buttonXpath = '/html/body/div[2]/div/div[1]/div/div[5]/div/div[1]/section/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/div[1]/section/a/article/div[8]/div/div/button'
        producto = "Cafetera"
        self.browser.get(url)
        inputName = self.browser.find_element(By.XPATH, inputXpath)
        inputName.send_keys(producto, Keys.ENTER)
        button = self.browser.find_element(By.XPATH, buttonXpath)
        self.assertIn('Agregar al carrito', button)


if __name__ == '__main__':
    unittest.main(verbosity=2)
