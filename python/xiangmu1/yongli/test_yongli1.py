import pytest
from xiangmu1.yemian.denglu import denglu
import time
import os
class TestClass1:
    def test_01(self):
        lp = denglu()
        lp.dakai("http://115.28.108.130/newecshop/admin/privilege.php?act=login")
        time.sleep(1)
        lp.do_denglu("admin", "hulaoshi2022")

    def test_02(self):
        pass

    if __name__=="__main__":
        pytest.main(["test_yongli1.py", '--alluredir', './result', '--clean-alluredir'])
        os.system('allure generate ./result/ -o ./report_allure/ --clean')