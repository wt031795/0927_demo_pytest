import pytest
from page.collection_page import CollectionGoods
from common.method import open_app
from page.receiving_address_page import ReceivingAddress
from time import sleep


class TestCollection:
    def setup_method(self):
        # 打开app
        driver = open_app()
        self.ecshop = CollectionGoods(driver)
        self.address = ReceivingAddress(driver)
        # 登录
        self.ecshop.login()
        self.ecshop.input_username("yehong")
        self.ecshop.input_password("yehong123")
        self.ecshop.click_login()

    @pytest.mark.run(order=1)
    def test_show_receiving_address(self):
        '''测试查看收货人地址'''
        sleep(3)
        self.address.click_receiving_address()  # 点击收货地址管理
        self.address.click_show_address()  # 点击查看
        result = self.address.get_collection_text()
        assert result == result

    @pytest.mark.run(order=2)
    def test_add_receiving_address(self):
        '''测试新增收货人地址'''
        sleep(3)
        self.address.click_receiving_address()  # 点击收货地址管理
        self.address.click_add_receiving_address()  # 点击新增收货地址
        self.address.click_receiving_name()  # 输入收货人姓名
        self.address.click_tel_num()  # 输入电话号码
        self.address.click_post_code()  # 输入邮编
        self.address.click_now_place()  # 点击所在地区
        self.address.click_country()  # 选择国家
        self.address.click_province()  # 选择省
        self.address.click_city()  # 选择市
        self.address.click_district()  # 选择区
        self.address.click_now_address()  # 详细地址
        self.address.click_save_address()  # 保存
        result = self.address.get_collection_text()
        assert result == result

    @pytest.mark.run(order=3)
    def test_change_receiving_address(self):
        '''测试修改收货人地址'''
        sleep(3)
        self.address.click_receiving_address()  # 点击收货地址管理
        self.address.click_show_address()  # 点击查看
        self.address.change_receiving_name()  # 点击修改收货人姓名
        self.address.save()  # 点击保存
        result = self.address.get_collection_text()
        assert result == result

    @pytest.mark.run(order=4)
    def test_delete_receiving_address(self):
        '''测试删除地址'''
        self.address.click_receiving_address()  # 点击收货地址管理
        self.address.click_show_address()  # 点击查看
        self.address.click_delete_address()  # 删除地址
        result = self.address.get_collection_text()
        assert result == result


if __name__ == '__main__':
    pytest.main()
