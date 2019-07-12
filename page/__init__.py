# 初始化
from selenium.webdriver.common.by import By

"""以下为登录页面元素数据"""
# 手机号
login_phone = (By.ID, "com.vcooline.aike:id/etxt_username")
# 密码
login_pwd = (By.ID, "com.vcooline.aike:id/etxt_pwd")
# 登录按钮
login_btn = (By.ID, "com.vcooline.aike:id/btn_login")
