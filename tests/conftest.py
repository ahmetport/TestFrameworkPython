import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

"""confest dosyasının amacı driver testlerden izole etmek"""

@pytest.fixture(scope="class")# sadece bu classı çalıştır driver sadece orda çalışsın
def setup(request,browser,environment):  #homepage classı ile iletişime geçmesi için request kullanıyoruz
    if browser == "chrome":  # browser chromr eşit ise
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox": # TERMİNALE test scriptimi yazdıktan sonra --browser firefox yazınca firefox da çalıştırır
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "microsoft":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    else:
        print("HEY AMİGO BAKABAYAŞİİİİ")

    if environment is None :
        print("environment girmediniz testi nasıl hangi ortamda çalıştıralım")
    else:
        if environment == "dev":
            base_url="https://dev-demowebshop.tricentis.com"  #böyle bir alan olmadıgı için çalışmaz
        elif environment == "qa":
            base_url="https://qa-demowebshop.tricentis.com"
        elif environment == "test":
            base_url = "https://test-demowebshop.tricentis.com"
        elif environment == "prod":
            base_url = "https://demowebshop.tricentis.com"  # sadece burda testim çalışır canlı oldugu için şirketlrtde her ortam vardır ama
        else:
            print("environment degeri hatalı")


    #driver.get("https://demowebshop.tricentis.com/") base url olunca burayı kapattık
    driver.maximize_window()
    request.cls.driver = driver # reguest çagıran classlara bu driveri ver bu driveri kullansınlar
    request.cls.baseurl=base_url
    yield
    driver.quit()

def pytest_addoption(parser): #ilk önce başka browserlardada çalışşsın diye parser yaptık
    parser.addoption("--browser")
    parser.addoption("--env") #environment testlerimiz için çok önemli çünkü canlıda testlerimizi çalıştıramayız
                              #hangi env çalıştırmk istersek orda çalıştırırız terminale bunu girerek

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser") #request kullanarak browsere terminalden kullanabiliriz

@pytest.fixture(scope="class", autouse=True)
def environment(request):
    return request.config.getoption("--env")


