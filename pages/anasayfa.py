from selenium.webdriver.common.by import By


class Anasayfa:
    def __init__(self,driver):
        self.driver=driver

    def gift_card_olmayan_urune_tikla(self):
        self.driver.find_element(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()