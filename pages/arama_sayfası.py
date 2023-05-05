import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageBase import PageBase

class AramaSayfasi(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    ARAMA_KUTUSU=(By.XPATH,"//input[@id='small-searchterms']")
    ARAMA_MESAJI=(By.CSS_SELECTOR,"div.search-results")

    def arama_yap(self,kelime):
        arama_kutusu=self.driver.find_element(*AramaSayfasi.ARAMA_KUTUSU)
        arama_kutusu.send_keys(kelime)
        arama_kutusu.send_keys(Keys.ENTER)

    def mesaj_ver(self):
        mesaj=self.driver.find_element(*AramaSayfasi.ARAMA_MESAJI).text.strip()
        return mesaj






