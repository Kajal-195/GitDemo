import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\Users\C5295630\AppData\Local\Programs\Python\Python39\Scripts")
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()