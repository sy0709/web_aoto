# import pytest
# import time
# # -m参数后面跟着标签名'-m','标签名','--reruns','2','--reruns-delay','5',
# pytest.main(["-s","-v",
#             "--html=Outputs/HTML_reports/report.html",
#             "--alluredir=Outputs/allure_reports"])

import pytest
import os
import time
if __name__ == '__main__':
    # 当前路径
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    # 测试用例路径
    TestCase_dir = current_dir+"/TestCases/login"
    # 报表路径
    report_dir = "--html="+current_dir+"/Outputs/HTML_reports/%sreport.html"%time.strftime("%Y_%m_%d_%H_%M_%S")
    allure_dir = "--alluredir="+current_dir+"/Outputs/allure_reports/%sallure"%time.strftime("%Y_%m_%d_%H_%M_%S")
    html_report_dir = "--html="+"/Outputs/HTML_reports/%sreport.html"%time.strftime("%Y_%m_%d_%H_%M_%S")
    # 执行用例
    # 一、拼接html报告的绝对路径
    # pytest.main(['-s', '-v', '--reruns', '2', '--reruns-delay','5','-m', 'run', report_dir])

    # 二、使用相对路径，路径相对于rootdir: C:\Users\admin\Desktop\qcd_webAuto_pytest
    # pytest.main(['-s', '-v', '--reruns', '2', '--reruns-delay', '5', r'--html=Outputs\HTML_reports\reports.html'])
    pytest.main(['-s', '-v', '--reruns', '2', '--reruns-delay', '5', html_report_dir])
    # 三、指定运行的测试子集 运行单个子目录 运行测试有很多方式，不但可以选择运行某个测试目录、文件、类中的测试，还可以选择运行某一个测试用例
    # pytest.main(['-s', '-v', 'TestCases/login/','-m','run','--reruns', '2', '--reruns-delay', '5', report_dir])

    # 四、运行单个测试文件
    # pytest.main(['TestCases/login/test_login.py'])

    # 五、运行单个类或单个函数,如果不希望测试子集中的所有测试，只想指定运行其中一个，则在函数或类名后面再加上::符号和方法名
    # pytest.main(['TestCases/login/test_login.py::Test_2_Link'])

    # 六、运行单个测试类中的测试方法：如果不希望运行测试类中的所有测试，只想指定运行其中一个，则在类名后面再加上::符号和方法名
    # pytest.main(['TestCases/login/test_login.py::Test_1_Login::test_2_login_True'])

    # 输出allure报告
    # pytest.main(['-s', '-v', '--reruns', '2', '--reruns-delay', '5', '-m', 'run', report_dir, r'--alluredir=Outputs\allure_reports'])

    # pytest.main(['-s', '-v', '--reruns', '2', '--reruns-delay', '5', '-m', 'run', report_dir, allure_dir])