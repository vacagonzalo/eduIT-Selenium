from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.felixcatinsurance.com/"
inputXpath = "/html/body/div[6]/div/div[2]/article/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/form/div/input"
catName = "Felix"
pageLoadTime = 5
demoTime = 5


def main():
    with webdriver.Firefox() as browser:
        try:
            browser.get(url)
            sleep(pageLoadTime)
            inputName = browser.find_element(By.XPATH, inputXpath)
            inputName.send_keys(catName, Keys.ENTER)
            sleep(demoTime)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
