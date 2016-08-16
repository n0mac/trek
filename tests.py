import unittest
from selenium import webdriver
import page
import time
import pymssql
from selenium.webdriver.common.keys import Keys

class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://admin-mountain-trek-test.mev.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_functionality(self):
        login_page = page.LoginPage(self.driver)
        practical_guide_page = page.PracticalGuidePage(self.driver)
        forgot_password = page.ForgotPasswordFunctionality(self.driver)
        asserts = page.AssertIDs(self.driver)

        assert asserts.login_page_title() in self.driver.page_source

        '''login_page.input_email_sign_in("test1@mev.com")
        login_page.input_password_field("qweqwe123")
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(4)

        assert asserts.validation_error() in self.driver.page_source

        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi@mev.com")
        login_page.clear_password_field()
        login_page.input_password_field("qweqwe123")
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(4)

        assert asserts.validation_error() in self.driver.page_source

        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi+1@mev.com")
        login_page.clear_password_field()
        login_page.input_password_field("qweqwe123")
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(4)

        assert asserts.not_active_admin_error() in self.driver.page_source

        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi@mev.com")
        login_page.clear_password_field()
        login_page.input_password_field("qweqweqwe")
        login_page.click_login_button()
        time.sleep(4)

        assert asserts.practical_guide_page_opened() in self.driver.page_source

        practical_guide_page.click_logout()

        forgot_password.click_forgot_password()
        forgot_password.input_forgot_email("iaroslav.antoshevskyi@mev.com")
        forgot_password.click_send_email()
        forgot_password.click_go_to_admin()
        time.sleep(10)
        forgot_password.open_gmail_in_new_tab()
        forgot_password.enter_email_gmail("iaroslav.antoshevskyi@mev.com")
        forgot_password.click_next()
        forgot_password.enter_email_pwd("histar777")
        forgot_password.click_sign_in()
        forgot_password.click_correct_mail()
        forgot_password.click_reset_password_mail()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        title=self.driver.title
        forgot_password.input_new_pwd("qq")
        forgot_password.input_confitm_pwd("qq")
        forgot_password.click_reset_your_password()
        time.sleep(1)
        forgot_password.clear_new_pwd()
        forgot_password.input_new_pwd("qweqwe123")
        forgot_password.clear_confirm_pwd()
        forgot_password.input_confitm_pwd("qweqweqwe")
        forgot_password.click_reset_your_password()
        time.sleep(1)
        forgot_password.clear_new_pwd()
        forgot_password.input_new_pwd("qweqweqwe")
        forgot_password.clear_confirm_pwd()
        forgot_password.input_confitm_pwd("qweqweqwe")
        forgot_password.click_reset_your_password()
        forgot_password.click_go_to_admin()'''

        login_page.input_email_sign_in("iaroslav.antoshevskyi@mev.com")
        login_page.input_password_field("qweqweqwe")
        time.sleep(0.3)
        login_page.click_login_button()
        time.sleep(4)
        3367211693
        assert asserts.practical_guide_page_opened() in self.driver.page_source
        time.sleep(4)
        #practical_guide_page.click_burger()
        #practical_guide_page.click_burger()
        practical_guide_page.click_dots_button()
        practical_guide_page.click_create_new_guide()
        practical_guide_page.click_dots_button()
        practical_guide_page.click_create_new_guide()
        practical_guide_page.upload_video("/Users/user/video/test_video.mp4")
        practical_guide_page.input_name("name1")
        time.sleep(2)
        practical_guide_page.input_categories("Detox")
        #practical_guide_page.input_author("Simon Shave")
        practical_guide_page.click_save_button()
        liss = self.driver.find_element_by_css_selector("input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-invalid-field.x-form-invalid-field-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
        liss.send_keys("ggaga")
        for li in liss:
            print (li.get_attribute('class'))
            #li.click()






