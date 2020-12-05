from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions, Chrome

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome("/Users/reonoldpetrenko/PycharmProjects/crud/chromedriver", chrome_options=opt)
homepage = "localhost:5000"


def navigation_test():
    driver.get(homepage)
    try:
        assert driver.title == "Test Employee Page"
    except AssertionError as e:
        print("Assertion failed", e)
    driver.close()


def add_employee_test():
    driver.get(homepage)
    driver.find_element_by_xpath("./[text()='Add']")


def edit_employee_test():
    pass


def delete_employee_test():
    pass


if __name__ == "__main__":
    navigation_test()
