import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
@pytest.mark.usefixtures("setup")
class Testhomepage:
    def test_menu_items(self):
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS", "JEWELRY",
                         "GIFT CARDS"]
        elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.top-menu > li > a")
        actual_menu_items = []  # bi tane liste açıp gelen elemntleri buraya ekliyoruz

        for i in elements:
            actual_menu_items.append(i.text)
            print(actual_menu_items)
            sleep(3)

        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_menu_items[i]

    def test_urunetikla_urunismiile_urunfiyatini_karsilastir(self):
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        ilkurun_linki=self.driver.find_element(By.CSS_SELECTOR,"div.product-item h2 a")
        urun_ismi=ilkurun_linki.text
        print(urun_ismi)
        urunfiyati=self.driver.find_element(By.CSS_SELECTOR,"span.price.actual-price").text
        print(urunfiyati)
        ilkurun_linki.click()
        urunismi_detaysayfasi=self.driver.find_element(By.CSS_SELECTOR,"div.product-name h1").text.strip()
        print(urunismi_detaysayfasi)
        urunfiyat_detaysayfasi=self.driver.find_element(By.CSS_SELECTOR,"div.product-price span").text.strip()
        print(urunfiyat_detaysayfasi)

        assert urun_ismi == urunismi_detaysayfasi
        assert urunfiyati == urunfiyat_detaysayfasi

















