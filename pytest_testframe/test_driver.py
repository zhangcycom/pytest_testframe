import pytest
import os

if __name__=="__main__":
    # pytest.main(["-vs","./test_script/login/test_Django_login.py","--alluredir=./test_report/tmp/report"])
    pytest.main(["-vs","./test_script/login/test_Django_login.py"])
    # os.system("allure generate  ./test_report/tmp/report")