import pytest
import os
import sys

sys.path.append(os.getcwd())
from page.page_login import PageLogin
import pytest


def get_data():
    return [("17600919712", "123456"), ("17600919711", "123456"), ("17600919712", "1234"),
            ("", "123456"), ("17600919712", ""), ("", ""), ("176009197123", "123456"), ("17600919712", "1234567")]


class TestLogin(object):
    # 初始化
    def setup_class(self):
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test_login(self, phone, pwd):
        # 调用登录业务方法
        self.login.page_login(phone, pwd)
