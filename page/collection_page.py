from common.method import Base
from time import sleep


class CollectionGoods(Base):
    '''制作定位器'''
    goods_one_loc = ("id", "com.insthub.ecmobile:id/good_cell_photo_one")  # 第一个商品定位器
    add_collection_loc = ("id", "com.insthub.ecmobile:id/collection_button")  # 添加收藏定位器
    photo_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabfour")  # 右下角最后一个按钮定位器
    user_info_loc = ("id", "com.insthub.ecmobile:id/profile_head_photo")  # 用户中心头像定位器
    username_loc = ("xpath", "//*[@text='用户名']")  # 输入用户名定位器
    password_loc = ("id", "com.insthub.ecmobile:id/login_password")  # 输入密码定位器
    login_loc = ("xpath", "//*[@text='登录']")  # 点击登录定位器
    home_page_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabone")  # 左下角第一个按钮定位器
    back_loc = ("id", "com.insthub.ecmobile:id/top_view_back")  # 返回按钮定位器
    my_collection_loc = ("xpath", "//*[@text='我的收藏']")  # 点击我的收藏
    edit_loc = ("xpath", "//*[@text='编辑']")  # 编辑定位器
    delete_collection_loc = ("id", "com.insthub.ecmobile:id/collect_item_remove1")  # 删除定位器
    delete_back_loc = ("id", "com.insthub.ecmobile:id/collect_back")  # 删除后返回按钮定位器
    collection_loc = ("id", "com.insthub.ecmobile:id/collect_item_image1")  # 获取id属性
    money_loc = ("xpath", "//*[contains(@text, '￥')]")  # 获取商品价格
    complex_loc = ("xpath", "//*[@text='完成']")  # 点击完成

    def login(self):
        '''登录'''
        self.click(self.photo_loc)
        self.click(self.user_info_loc)

    def click_complex(self):
        '''删除之后点击完成'''
        self.click(self.complex_loc)

    def user_info(self):
        '''点击个人中心'''
        self.click(self.photo_loc)

    def my_collection(self):
        '''点击我的收藏'''
        self.click(self.my_collection_loc)

    def click_edit(self):
        '''点击编辑'''
        self.click(self.edit_loc)

    def click_delete_collection(self):
        '''点击删除'''
        self.click(self.delete_collection_loc)

    def delete_back(self):
        '''点击删除后返回'''
        self.click(self.delete_back_loc)

    def input_username(self, username):
        '''输入用户名'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码'''
        self.send_keys(self.password_loc, password)

    def click_login(self):
        '''点击登录'''
        self.click(self.login_loc)

    def click_collection_goods(self):
        '''点击收藏商品'''
        self.click(self.goods_one_loc)
        self.click(self.add_collection_loc)

    def click_home_page(self):
        '''点击首页'''
        self.click(self.home_page_loc)

    def click_back(self):
        '''点击返回'''
        self.click(self.back_loc)

    def get_collection_text(self):
        """获取id属性"""
        self.get_element_file(self.collection_loc)

    def get_find_all_money(self):
        '''获取所有收藏商品的价格'''
        return self.get_goods_num(self.money_loc)


if __name__ == '__main__':
    from common.method import open_app

    driver = open_app()  # 打开app
    sleep(2)
    ecshop = CollectionGoods(driver)  # 实例化类

    ecshop.login()  # 登录
    sleep(2)

    username = "yehong"  # 输入用户名
    ecshop.input_username(username)

    password = "yehong123"  # 输入密码
    ecshop.input_password(password)
    sleep(2)

    ecshop.click_login()  # 点击登录
    sleep(2)
    '''添加收藏'''
    ecshop.click_home_page()  # 点击首页
    sleep(10)

    ecshop.click_collection_goods()  # 点击收藏商品
    sleep(2)

    '''查看收藏夹'''
    ecshop.click_back()  # 点击返回
    sleep(2)
    ecshop.user_info()  # 点击个人中心
    sleep(2)
    ecshop.my_collection()  # 点击我的收藏
    sleep(2)

    '''删除收藏'''
    ecshop.click_edit()  # 点击编辑按钮
    sleep(2)

    ecshop.click_delete_collection()  # 点击删除按钮
    sleep(2)

    ecshop.delete_back()  # 点击删除后返回
    sleep(2)

    ecshop.close_app()  # 关闭app
