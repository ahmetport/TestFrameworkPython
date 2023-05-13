import unittest

import pytest
from ddt import ddt, data, unpack

from pages.arama_sayfası import AramaSayfasi
from utilities.ExcelYardımcisi import ExcelYardımcı


@pytest.mark.usefixtures("setup")
@ddt
class TestArama(unittest.TestCase):

    # Bu örnekteki gibi veriyi elle yazmak iyi uygulama değil.
    # Bunun yerine aşağıdaki gibi excelden veriyi almak daha doğru
   # @data(("ab", "Search term minimum length is 3 characters"), ("abc", "No products were found that matched your criteria."))
   # @unpack
   # def test_arama_uyari_verir(self, kelime, beklenen_mesaj):
   #     self.driver.get("https://demowebshop.tricentis.com/")
   #     arama = AramaSayfasi(self.driver)
   #     arama.arama_yap(kelime)
   #     mesaj = arama.arama_uyari_mesajini_ver()
   #     assert mesaj == beklenen_mesaj

    @data(*ExcelYardımcı.excel_listeler_listesine_cevir("./testdata/arama.xlsx", "Sayfa1"))
    @unpack
    def test_arama(self, senaryoturu, kelime, beklenen_mesaj):
        self.driver.get("https://demowebshop.tricentis.com/")
        arama = AramaSayfasi(self.driver)
        arama.arama_yap(kelime)
        if senaryoturu.lower() == "negatif":
            mesaj = arama.arama_uyari_mesajini_ver()
            assert mesaj == beklenen_mesaj
        elif senaryoturu.lower() == "pozitif":
            urun_isimleri = arama.aranan_urun_isimlerini_liste_ver()
            for isim in urun_isimleri:
                assert kelime.lower() in isim.lower()




