from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.easy.com.ar/"
inputXpath = '//*[@placeholder="¡Hola! ¿Qué estás buscando?"]' 
producto = "Cafetera"
pageLoadTime = 5
demoTime = 5


def main():
    with webdriver.Firefox() as browser:
        try:
            browser.get(url)
            browser.maximize_window()
            sleep(pageLoadTime)
            inputName = browser.find_element(By.XPATH, inputXpath)
            inputName.send_keys(producto, Keys.ENTER)
            sleep(demoTime)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
