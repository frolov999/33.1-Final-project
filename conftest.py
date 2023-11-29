import pytest
from selenium import webdriver
from pages.registr_page import RegistrPage
from pages.auth_page import AuthPage



@pytest.fixture(scope="session")
def selenium():
    driver = webdriver.Chrome(executable_path="C:/test/chromedriver.exe")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def registr(selenium):
    registr = RegistrPage(selenium)
    return registr


@pytest.fixture(scope="session")
def auth(selenium):
    auth = AuthPage(selenium)
    return auth
