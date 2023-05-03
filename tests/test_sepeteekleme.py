import pytest
import time
import re

from selenium.webdriver.common.by import By

from pages.anasayfa import Anasayfa
from pages.Urun_DetaySayfa import Urun_DetaySayfa


@pytest.mark.usefixtures("setup")
class TestSepeteEkleme:
    #@pytest.fixture(autouse=true)
    #def class_setup(self):
     #   self.anasayfa=Anasayfa(self.driver) #object sadece burda oluşturduk her def fonksiyonunda kullanalım diye

    def test_urundetaylari(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        anasayfa=Anasayfa(self.driver)
        urun_detay_sayfasi=Urun_DetaySayfa(self.driver)

        anasayfa.gift_card_olmayan_urune_tikla()
        oncesi=urun_detay_sayfasi.sepetteki_urun_sayisini_ver()
        quantity=urun_detay_sayfasi.quantity_sayisini_ver()
        urun_detay_sayfasi.AddTo_cart_Tikla()
        time.sleep(3)
        sonrasi = urun_detay_sayfasi.sepetteki_urun_sayisini_ver()

        assert sonrasi == (oncesi + quantity)

    #biz burda page object model kullandık ve iki tane ayrı page oluşturduk locateleri oraya yazdık
    #test sayfasındada aynı cucumberda oldugu gibi object oluşturup ordaki def ile oluşturdugumuz
    #metod veya fonksiyon onları buraya çagırdık page object model guzel tarafı test classının clean
    #olması ve fazle kod olmaması anlaşılır olaması




        #self.driver.find_element(By.XPATH,"//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()
        #sepetteki_urunsayisi=self.driver.find_element(By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)").text
        #sepetteki_urunsayisi=re.findall(r'\d+', sepetteki_urunsayisi)#bu bir list döneceginden
        #oncesi=int(sepetteki_urunsayisi[0])#işlk index bize dönsün diyoruz

        #quantity=self.driver.find_element(By.CSS_SELECTOR,"input[id$='EnteredQuantity']").get_attribute('value')
        #quantity=int(re.findall(r'\d+',quantity)[0])  # $ işareti bununla biten demek locate alırken

        #self.driver.find_element(By.CSS_SELECTOR,"input[id^='add-to-cart-button']").click()
        #time.sleep(3) #^ işareti bunla başlayan demek

        #add to carta tıkladıktan sonraki durum için
        #sepetteki_urunsayisi = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        #time.sleep(2)
        #sepetteki_urunsayisi = re.findall(r'\d+', sepetteki_urunsayisi)
        #sonrasi = int(sepetteki_urunsayisi[0])


    #locateler tekrar alınacak sıkıntı var
