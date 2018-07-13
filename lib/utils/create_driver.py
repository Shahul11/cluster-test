import pytest
from selenium.webdriver import  Chrome,Firefox

def get_driver_instance():
    browser_type=pytest.config.option.type.lower()
    env=pytest.config.option.env.lower()


    if env=='local':
        if browser_type =='firefox':
            driver=Firefox('./browsers_servers/geckodriver.exe')
        elif browser_type =='chrome':
            driver=Chrome('./browsers_servers/chromedriver.exe')
        else:
            print("Invalid Browser Option")
    elif env=='remote':
        print('Add features for remote execution')
    else:
        print('Invalid Environment Option')
    driver.maximize_window()

  #  driver.implicit_wait(30)
    driver.get("http://localhost/login.do")

    return  driver


