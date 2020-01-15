from common.method import Base
from time import sleep
from page.collection_page import CollectionGoods
from common.faker_data import Fake


class ReceivingAddress(Base):
    receiving_address_loc = ("xpath", "//*[@text='收货地址管理']")  # 收货地址管理定位器
    add_receiving_address_loc = ("id", "com.insthub.ecmobile:id/address_manage_add")  # 点击新增地址
    receiving_name_loc = ("xpath", "//*[@text='收货人姓名（必填）']")  # 收货人姓名
    tel_num_loc = ("xpath", "//*[@text='电话号码（必填）']")  # 电话号码
    post_code_loc = ("xpath", "//*[@text='邮政编码']")  # 邮政编码
    now_place_loc = ("xpath", "//*[@text='所在地区']")  # 所在地区
    country_loc = ("xpath", "//*[@text='中国']")  # 选择中国
    province_loc = ("id", "com.insthub.ecmobile:id/city_item_name")  # 定位省
    city_loc = ("id", "com.insthub.ecmobile:id/city_item_name")  # 定位市
    district_loc = ("id", "com.insthub.ecmobile:id/city_item_name")  # 定位区
    now_address_loc = ("xpath", "//*[@text='详细地址（必填）']")  # 定位详细地址
    save_address_loc = ("id", "com.insthub.ecmobile:id/add_address_add")  # 保存地址
    show_address_loc = ("class name", "android.widget.LinearLayout")  # 点击地址
    change_receiving_name_loc = ("id", "com.insthub.ecmobile:id/address_manage2_name")  # 修改收获人姓名
    click_save_loc = ("xpath", "//*[@text='保存']")  # 点击保存
    delete_address_loc = ("xpath", "//*[@text='删除地址']")  # 删除地址
    get_text_loc = ("id", "com.insthub.ecmobile:id/address_manage_item_layout")  # 获取文本属性

    random = Fake()  # 实例化faker类

    def click_receiving_address(self):
        '''点击收货地址'''
        self.click(self.receiving_address_loc)

    def click_add_receiving_address(self):
        '''点击新增收货地址'''
        self.click(self.add_receiving_address_loc)

    def click_receiving_name(self):
        '''点击输入收货人姓名'''
        self.send_keys(self.receiving_name_loc, self.random.get_username())

    def click_tel_num(self):
        '''点击输入电话号码'''
        self.send_keys(self.tel_num_loc, self.random.get_phone())

    def click_post_code(self):
        '''点击输入邮政编码'''
        self.send_keys(self.post_code_loc, self.random.get_post())

    def click_now_place(self):
        '''点击所在地区'''
        self.click(self.now_place_loc)

    def click_country(self):
        '''点击国家'''
        self.click(self.country_loc)

    def click_province(self):
        '''点击省'''
        self.click_random_elements(self.province_loc)

    def click_city(self):
        '''点击市'''
        self.click_random_elements(self.city_loc)

    def click_district(self):
        '''点击区'''
        self.click_random_elements(self.district_loc)

    def click_now_address(self):
        '''点击详细地址'''
        self.send_keys(self.now_address_loc, self.random.get_address())

    def click_save_address(self):
        '''点击保存地址'''
        self.click(self.save_address_loc)

    def click_show_address(self):
        '''点击查看地址'''
        for i in self.show_address_loc:
            if i == 0:
                pass
            else:
                self.click_random_elements(self.show_address_loc)

    def change_receiving_name(self):
        '''修改收获人姓名'''
        self.send_keys(self.change_receiving_name_loc, self.random.get_username())

    def save(self):
        '''点击保存'''
        self.click(self.click_save_loc)

    def click_delete_address(self):
        '''删除地址'''
        self.click(self.delete_address_loc)
        
    def get_collection_text(self):
        """获取id属性"""
        self.get_element_file(self.get_text_loc)


if __name__ == '__main__':
    from common.method import open_app

    driver = open_app()  # 打开app
    sleep(2)

    ecshop = CollectionGoods(driver)  # 实例化收藏类
    address = ReceivingAddress(driver)  # 实例化收藏地址类

    ecshop.login()  # 登录
    sleep(2)

    username = "yehong"  # 输入用户名
    ecshop.input_username(username)

    password = "yehong123"  # 输入密码
    ecshop.input_password(password)

    ecshop.click_login()  # 点击登录
    sleep(4)

    ecshop.user_info()  # 点击个人中心
    sleep(2)
    '''查看收货人地址'''
    address.click_receiving_address()  # 点击收货地址管理

    '''新增收货地址'''
    address.click_add_receiving_address()  # 点击新增收货地址

    address.click_receiving_name()  # 输入收货人姓名

    address.click_tel_num()  # 输入电话号码

    address.click_post_code()  # 输入邮编

    address.click_now_place()  # 点击所在地区

    address.click_country()  # 选择国家

    address.click_province()  # 选择省

    address.click_city()  # 选择市

    address.click_district()  # 选择区

    address.click_now_address()  # 详细地址

    address.click_save_address()  # 保存

    '''修改地址'''
    address.click_show_address()  # 点击查看

    address.change_receiving_name()  # 点击修改收货人姓名

    address.save()  # 点击保存

    '''删除地址'''
    sleep(3)
    address.click_show_address()  # 点击查看

    address.click_delete_address()  # 删除地址

    sleep(3)
    address.close_app()  # 关闭app
