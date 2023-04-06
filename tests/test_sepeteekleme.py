import pytest
import time
import re

from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestSepeteEkleme:

    def test_urundetaylari(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class='item-box']//h2/a[not(contains(text(), 'Gift Card'))]").click()
        sepetteki_urunsayisi=self.driver.find_element(By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)").text
        sepetteki_urunsayisi=re.findall(r'\d+', sepetteki_urunsayisi)
        oncesi=int(sepetteki_urunsayisi[0])

        quantity=self.driver.find_element(By.CSS_SELECTOR,"input[id$='EnteredQuantity']").get_attribute('value')
        quantity=int(re.findall(r'\d+',quantity)[0])

        self.driver.find_element(By.CSS_SELECTOR,"input[id^='add-to-cart-button']").click()
        time.sleep(3)
        sepetteki_urunsayisi = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        time.sleep(2)
        sepetteki_urunsayisi = re.findall(r'\d+', sepetteki_urunsayisi)
        sonrasi = int(sepetteki_urunsayisi[0])

        assert sonrasi == (oncesi+quantity)

    #locateler tekrar alınacak sıkıntı var
