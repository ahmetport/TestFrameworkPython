from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    request.cls.driver=driver #soldaki driver bizim verdigimiz isim sagdaki ise yukardaki driver

    yield
    driver.quit()
