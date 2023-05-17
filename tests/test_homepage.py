import pytest
import softest
from pages.anasayfa import Anasayfa
from pages.urun_detay_sayfasi import UrunDetaySayfasi


@pytest.mark.usefixtures("setup")
class TestHomepage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.anasayfa = Anasayfa(self.driver)

    #@pytest.mark.smoke #terminale -m smoke dedigimde sadece bu testi çalıştırır
    def test_ust_menu_linklerini_dogrula(self):
        print("url ="+self.baseurl) #hangi url çalışıp çalışmadıgını kontrol için yazdık buraya
        #self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.get(self.baseurl)
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]

        actual_menu_items = self.anasayfa.ust_menu_isimlerini_liste_ver()
        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_menu_items[i]

    #@pytest.mark.smoke
    def test_urun_ismine_tiklayinca_urun_detaylari_sayfasi_acilir(self):
        #self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.get(self.baseurl)
        urun_ismi = self.anasayfa.ilk_urun_ismini_ver()
        urun_fiyati = self.anasayfa.ilk_urun_fiyatini_ver()
        urun_detay_sayfasi = self.anasayfa.ilk_urun_ismine_tikla()
        print("Anasayfa urun ismi: " + urun_ismi)
        print("anasayfa urun fiyati: " + urun_fiyati)
        urun_ismi_detay_sayfasi = urun_detay_sayfasi.urun_ismini_ver()
        urun_fiyat_detay_sayfasi = urun_detay_sayfasi.urun_fiyatini_ver()
        self.soft_assert(self.assertEqual, urun_ismi, urun_ismi_detay_sayfasi, "Urun ismi detay sayfasinda farkli")
        self.soft_assert(self.assertEqual, urun_fiyati, urun_fiyat_detay_sayfasi, "Urun fiyati detay sayfasinda farkli")
        self.assert_all()















