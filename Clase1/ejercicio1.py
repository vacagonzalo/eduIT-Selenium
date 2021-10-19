from time import sleep
from selenium import webdriver

url = "https://www.felixcatinsurance.com/"
pageLoadTime = 5


def main():
    with webdriver.Firefox() as browser:
        try:
            browser.get(url)
            sleep(pageLoadTime)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
