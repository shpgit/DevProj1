from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium.common.exceptions
from selenium.webdriver.common.by import By


def frontend_testing(user_id):
    web_user_name = None

    try:
        driver = webdriver.Chrome(service=Service("../prj_resources/chromedriver"))
        web_userid = f"http://127.0.0.1:5001/users/get_user_data/{user_id}"
        driver.get(web_userid)
        driver.implicitly_wait(5)

        web_user_name = driver.find_element(By.ID, value="user").text
        print(web_user_name)

    except selenium.common.exceptions.WebDriverException as webDriverErr:
        print(webDriverErr)
    finally:
        driver.close()
    return web_user_name


if __name__ == '__main__':
    frontend_testing(1)


