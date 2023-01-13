# 接口自动化
import os

import xToolkit,requests,pytest,allure
所有测试用例= xToolkit.xfile.read("接口用例.xls").excel_to_dict(sheet=1)
@pytest.mark.parametrize("单个测试用例",所有测试用例) #pytest 参数化机制
def test_case_exec(单个测试用例):
    print("执行测试用例：")
# 第一个测试用例=所有测试用例[0]
    接口响应 = requests.request(
        url = 单个测试用例['接口URL'],
        method = 单个测试用例['请求方式'],
        params= eval(单个测试用例['接口参数']),
        # json =第一个测试用例['json参数'],
        # headers =第一个测试用例['请求头']
    )
    print("接口实际响应内容：", 接口响应.text)
    # 断言
    assert 单个测试用例['预期状态码']==接口响应.status_code,'测试不通过，状态码不对'
if __name__ == '__main__':
    pytest.main([
        '-s',
        '-v',
        '--capture=sys',
        'jiekouzidonghua.py',
        '--clean-alluredir','--alluredir=allure-results',
    ])
    os.system(r"allure generate -c -o 测试报告")
