import pytest
from page.collection_page import CollectionGoods
from common.method import open_app


class TestCollection:
    def setup_method(self):
        # 打开app
        driver = open_app()
        self.ecshop = CollectionGoods(driver)
        # 登录
        self.ecshop.login()
        self.ecshop.input_username("yehong")
        self.ecshop.input_password("yehong123")
        self.ecshop.click_login()
        # # 点击首页
        self.ecshop.click_home_page()

    @pytest.mark.run(order=1)
    def test_add_collection(self):
        '''测试新增收藏'''
        self.ecshop.click_home_page()  # 首页
        self.ecshop.click_collection_goods()  # 收藏商品
        self.ecshop.click_back()  # 返回
        self.ecshop.user_info()  # 点击个人中心
        self.ecshop.my_collection()  # 点击我的收藏

    @pytest.mark.run(order=2)
    def test_show_collection(self):
        '''测试查看收藏'''
        self.ecshop.user_info()  # 点击个人中心
        self.ecshop.my_collection()  # 点击我的收藏
        result = self.ecshop.get_collection_text()  # 断言
        assert result == result

    @pytest.mark.run(order=3)
    def test_delete_collection(self):
        '''测试删除收藏'''
        self.ecshop.my_collection()  # 点击我的收藏
        num1 = self.ecshop.get_find_all_money()  # 获取所有的价格
        print(num1)
        self.ecshop.click_edit()  # 点击编辑
        self.ecshop.click_delete_collection()  # 点击删除
        self.ecshop.click_complex()  # 点击完成
        num2 = self.ecshop.get_find_all_money()  # 获取删除之后的价格
        print(num2)
        self.ecshop.delete_back()  # 点击返回
        '''断言'''
        assert num2 == num1 - 1


if __name__ == '__main__':
    pytest.main()
