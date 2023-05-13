import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

"""confest dosyasının amacı driver testlerden izole etmek"""

@pytest.fixture(scope="class")# sadece bu classı çalıştır driver sadece orda çalışsın
def setup(request): #homepage classı ile iletişime geçmesi için request kullanıyoruz
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    request.cls.driver = driver # reguest çagıran classlara bu driveri ver bu driveri kullansınlar
    yield
    driver.quit()


