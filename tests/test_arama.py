import pytest
import time
import unittest

from pages.arama_sayfası import AramaSayfasi
from ddt import ddt, data, file_data, idata, unpack





@pytest.mark.usefixtures("setup")
@ddt
class TestArama(unittest.TestCase):
    @data(*excelYardımcı.excel_listeler_listesine_cevir("./testdata/arama.xls","Sheet1"))
    @unpack

    def test_ikiharfli_üçharfli_aramayap(self,kelime,beklenen_mesaj):
        arama=AramaSayfasi(self.driver)
        arama.arama_yap(kelime)
        mesaj=arama.mesaj_ver()
        time.sleep(3)
        assert mesaj == beklenen_mesaj


