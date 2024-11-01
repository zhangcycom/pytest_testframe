#Django自动化测试平台selenium自动化测试脚本—pytest封装
#功能名称：登录
#版本：V2.1_参数化设置_相同处理过程，不同参数
#描述：正常异常用户登录
import pytest
from selenium import webdriver
#1、创建测试类
class Test_Django_Login():
#2、创建测试方法
    #登录初始化
    def setup_method(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    #正常登录测试方法


    @pytest.mark.parametrize('uname,pwd,state', (["atstudy", "51testing", 1], ["atstudy1", "51testing", 0]))
    def test_login_01(self,uname,pwd,state):
        self.driver.find_element_by_name('username').send_keys(uname)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
        # 统一检查点
        result = self.driver.current_url
        print(result)
        if state==1:
            assert result != self.url
        else:
            assert result == self.url
    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['test_Django_login_para1.py','-s','-v'])
