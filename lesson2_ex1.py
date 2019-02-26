from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    driver.close()    