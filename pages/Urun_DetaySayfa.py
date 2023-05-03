import re
from selenium.webdriver.common.by import By
from pages.PageBase import PageBase


class Urun_DetaySayfa(PageBase): #buraya pagebase yazdıgımızda (PageBase)normalde import et özelligi gelmeliydi
    #ama gelmedi ? kendimiz import ettik

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    SEPETTEKİ_ÜRÜN_SAYISI= (By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)")
    QUANTITY_SAYISINI_VER= (By.CSS_SELECTOR,"input[id$='EnteredQuantity']")
    ADTO_CART_BUTTON= (By.CSS_SELECTOR, "input[id^='add-to-cart-button']")

    #LOCATELERİ POM KULLANARAK DAHA ANLAŞILIR HALE GETİRDİK ARTIK DEGİŞİKLİK YAPMAK
    #İSTEDİGİMİZ ZAMAN YUKARDAN TEK YERDEN YAPABİLİRİZ

    def sepetteki_urun_sayisini_ver(self):
        sepetteki_urunsayisi=self.driver.find_element(*Urun_DetaySayfa.SEPETTEKİ_ÜRÜN_SAYISI).text
        sepetteki_urunsayisi=re.findall(r'\d+', sepetteki_urunsayisi)#bu bir list döneceginden
        return int(sepetteki_urunsayisi[0])#işlk index bize dönsün diyoruz ve artık return ediyoruz

    def quantity_sayisini_ver(self):
        quantity=self.driver.find_element(*Urun_DetaySayfa.QUANTITY_SAYISINI_VER).get_attribute('value')
        return int(re.findall(r'\d+',quantity)[0])  # $ işareti bununla biten demek locate alırken

    def AddTo_cart_Tikla(self):
        ButoneTikla=self.wait_element_visibility(Urun_DetaySayfa.ADTO_CART_BUTTON) #wait yapacak bunu yaparken
        ButoneTikla.click()#pageBase den aldıgı wait le 30 sn bekleyecek
        #self.driver.find_element(*Urun_DetaySayfa.ADTO_CART_BUTTON).click()