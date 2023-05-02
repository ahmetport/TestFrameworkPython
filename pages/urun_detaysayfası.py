import re
from selenium.webdriver.common.by import By


class UrunDetaySayfa:
    def __init__(self,driver):
        self.driver=driver

    def sepetteki_urun_sayisini_ver(self):
        sepetteki_urunsayisi=self.driver.find_element(By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)").text
        sepetteki_urunsayisi=re.findall(r'\d+', sepetteki_urunsayisi)#bu bir list döneceginden
        return int(sepetteki_urunsayisi[0])#işlk index bize dönsün diyoruz ve artık return ediyoruz

    def quantity_sayisini_ver(self):
        quantity=self.driver.find_element(By.CSS_SELECTOR,"input[id$='EnteredQuantity']").get_attribute('value')
        return int(re.findall(r'\d+',quantity)[0])  # $ işareti bununla biten demek locate alırken

    def AddTo_cart_Tikla(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[id^='add-to-cart-button']").click()