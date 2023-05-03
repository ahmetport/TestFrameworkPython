from selenium.webdriver.common.by import By

class Anasayfa:
    def __init__(self,driver):
        self.driver=driver
    GIFT_OLMAYAN_URUNU_TIKLA= (By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]")

    def gift_card_olmayan_urune_tikla(self):
        self.driver.find_element(*Anasayfa.GIFT_OLMAYAN_URUNU_TIKLA).click()

    #* işareti koymamızın sebebi python bu tuple açaçak o yuzden o tuple açsın buraya yerleştirsin