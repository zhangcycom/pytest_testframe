#****************************************************
#Django自动化测试平台selenium自动化测试脚本—pytes业务脚本t封装
#功能名称：新建组&新建用户
#版本：V1.0
#描述：新增小组+新建用户
#登录和退出浏览器执行一次
#****************************************************
import pytest
from selenium import webdriver

#1、创建业务流程测试类（独立+无序）
@pytest.mark.smoke1
class Test_add_group_user():
    #前置类方法
    def setup_class(self):
        self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.find_element_by_name('username').send_keys('atstudy')
        self.driver.find_element_by_name('password').send_keys('51testing')
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    #测试添加组
    @pytest.mark.run(order=2)
    def test_add_group(self):
        url = 'http://testplt.share.atstudy.com/admin/auth/group/add/'
        self.driver.get(url)
        self.driver.find_element_by_id('id_name').send_keys("group1")
        # 全选权限
        self.driver.find_element_by_id('id_permissions_add_all_link').click()
        self.driver.find_element_by_xpath('//*[@id="group_form"]/div/div/input[1]').click()
    #测试添加用户
    @pytest.mark.run(order=1)
    def test_add_user(self):
        url = 'http://testplt.share.atstudy.com/admin/auth/user/add/'
        self.driver.get(url)
        self.driver.find_element_by_id('id_username').send_keys("user")
        self.driver.find_element_by_id('id_password1').send_keys("123456Pwd")
        self.driver.find_element_by_id('id_password2').send_keys("123456Pwd")
        # 点击保存
        self.driver.find_element_by_xpath('//*[@id="user_form"]/div/div/input[1]').click()
    def teardown_class(self):
        self.driver.close()