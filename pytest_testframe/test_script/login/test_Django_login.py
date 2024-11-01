#Django自动化测试平台selenium自动化测试脚本—pytest封装
#功能名称：登录
#版本：V1.0
#描述：常量正常用户登录
import logging
import logging.config
import pytest
from selenium import webdriver
import time
import allure
#******************************************
#日志对象的初始化
#******************************************
logging.config.fileConfig('logger.conf')
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')

logger = logging.getLogger('main')

#1、创建测试类
@allure.feature("常量数据登录测试")
@pytest.mark.smoke
class Test_Django_Login():
#2、创建测试方法
    #登录初始化
    # def setup_method(self):
    #     self.url = "http://testplt.share.atstudy.com/admin/login/?next=/admin/"
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(self.url)
    #正常登录测试方法

    def test_login_01(self,browser):
        browser.find_element_by_name('username').send_keys('atstudy')
        root_logger.info("输入用户名atstudy")
        logger.info("输入用户名atstudy")
        browser.find_element_by_name('password').send_keys('51testing')
        root_logger.info("输入密码51testing")
        logger.info("输入密码51testing")
        browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
        root_logger.info("点击登录按钮")
        logger.info("点击登录按钮")
        # 检查点？
        result = browser.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/caption/a').text
        print(result)
        #3、通过断言进行判断
        root_logger.info("进行检查点验证")
        logger.info("进行检查点验证，实际结果为：测试平台，预期结果为："+result)

        assert result=="测试平台"

    # 异常登录测试方法—用户名不存在

    # def test_login_02(self,browser):
    #     #进行注销回到登录页面
    #     browser.find_element_by_xpath('//*[@id="user-tools"]/a[3]').click()
    #     #点击重新登录
    #     browser.find_element_by_xpath('//*[@id="content"]/p[2]/a').click()
    #     #重新登录
    #     browser.find_element_by_name('username').send_keys('atstudy1')
    #     browser.find_element_by_name('password').send_keys('51testing')
    #     browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    #     time.sleep(3)
    # #     # 检查点？
    # #     # result = self.driver.current_url
    # #     # assert result == self.url
    # #
    # #     #**********************************************************************************************
    # #     #异常处理方法1通过try-except进行异常处理
    #     try:
    #         result = browser.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/caption/a').text
    #         print(result)
    #         # 3、通过断言进行判断
    #         assert result == "测试平台"
    #     except Exception as e:
    #         result = browser.find_element_by_xpath('//*[@id="content"]/p').text
    #         # 断言：包含比对
    #         assert "请输入" in result

    #
    #     # **********************************************************************************************
    #     # 异常处理方法2：改变检查点：进行错误信息比对
    #     # result = self.driver.find_element_by_xpath('//*[@id="content"]/p').text
    #     # #     #断言：包含比对
    #     # assert "请输入" in result
    # #     # **********************************************************************************************
    # #     # 异常处理方法3：改变检查点：进行URL的比对
    # #     #获取当前页面的URL
    # def teardown_method(self):
    #     self.driver.close()

    def test_login_03(self,browser):
        browser.close()