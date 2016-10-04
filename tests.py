import time
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import HTMLTestRunner
import page


class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://admin-mountain-trek-test.mev.com/"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    '''def test_1practical_guide_functionality(self):
        self.driver.get(self.base_url)
        login_page = page.LoginPage(self.driver)
        practical_guide_page = page.PracticalGuidePage(self.driver)
        forgot_password = page.ForgotPasswordFunctionality(self.driver)
        cookbook_page = page.CookBookPage(self.driver)
        asserts = page.AssertIDs(self.driver)

        #assert asserts.login_page_title() in self.driver.page_source

        login_page.input_email_sign_in("test@mev.com")
        time.sleep(0.3)
        login_page.input_password_field("qweqwe123")
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(0.2)
        #time.sleep(4)

        assert asserts.validation_error() in self.driver.page_source

        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi@mev.com")
        login_page.clear_password_field()
        time.sleep(0.3)
        login_page.input_password_field("qweqwe123")
        time.sleep(0.3)
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(0.2)

        assert asserts.validation_error() in self.driver.page_source
        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi+1@mev.com")
        login_page.clear_password_field()
        time.sleep(0.3)
        login_page.input_password_field("qweqwe123")
        time.sleep(0.3)
        login_page.click_login_button()

        login_page.wait_until_ok_is_present()
        time.sleep(0.2)

        assert asserts.not_active_admin_error() in self.driver.page_source
        login_page.click_ok_button()

        login_page.clear_email_sign_in()
        login_page.input_email_sign_in("iaroslav.antoshevskyi@mev.com")
        login_page.clear_password_field()
        time.sleep(0.3)
        login_page.input_password_field("qweqweqwe")
        time.sleep(0.3)
        login_page.click_login_button()
        #time.sleep(4)
        practical_guide_page.wait_until_practical_guide_opened()
        assert asserts.practical_guide_page_opened() in self.driver.page_source

        practical_guide_page.click_logout()

        forgot_password.click_forgot_password()
        forgot_password.input_forgot_email("iaroslav.antoshevskyi@mev.com")
        forgot_password.click_send_email()
        forgot_password.click_go_to_admin()
        #time.sleep(10)
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
        forgot_password.click_go_to_admin()



        login_page.input_email_sign_in("test@mev.com")
        login_page.input_password_field("12345678")
        time.sleep(0.3)
        login_page.click_login_button()
        #time.sleep(6)
        practical_guide_page.wait_until_practical_guide_opened()
        assert asserts.practical_guide_page_opened() in self.driver.page_source

        practical_guide_page.click_burger()
        practical_guide_page.wait_until_practical_guide_opened()
        practical_guide_page.click_burger()
        time.sleep(1)


        practical_guide_page.click_dots_button()
        practical_guide_page.click_create_new_guide()
        practical_guide_page.upload_video("/Users/user/video/test_video.mp4")
        practical_guide_page.input_name("Solo322")
        #time.sleep(2)
        practical_guide_page.input_categories("Fitness")
        practical_guide_page.input_author("Bob Good")
        practical_guide_page.upload_featured_img("/Users/user/video/4396.jpg")
        practical_guide_page.input_featured_text("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        practical_guide_page.click_activate()
        practical_guide_page.click_wysywyg()
        practical_guide_page.enter_text_guide("Lorem")
        practical_guide_page.click_hyprlink_button()
        practical_guide_page.enter_hyper_link("test.com")
        liss = self.driver.find_elements_by_css_selector("span.x-btn-inner.x-btn-inner-default-small")
        time.sleep(0.3)
        liss[2].click()
        practical_guide_page.enter_text_guide(" Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        practical_guide_page.highlight_all()
        practical_guide_page.click_numbers()
        practical_guide_page.click_dots()
        #practical_guide_page.click_dots()
        practical_guide_page.click_header_one()
        practical_guide_page.highlight_all()
        practical_guide_page.click_header_two()
        practical_guide_page.click_wysywyg()
        practical_guide_page.clear_filters()
        practical_guide_page.highlight_all()
        practical_guide_page.click_mini_modal()
        practical_guide_page.enter_text_to_textarea("test text provided")
        liss2 = self.driver.find_elements_by_css_selector("span.x-btn-inner.x-btn-inner-default-small")
        time.sleep(0.3)
        liss2[2].click()


        #practical_guide_page.input_author("Bob Good")
        practical_guide_page.upload_new_video()
        #time.sleep(2)
        #practical_guide_page.choose_file("/Users/user/video/test_video.mp4")
        liss1 = self.driver.find_elements_by_class_name("x-form-file-input")
        liss1[2].send_keys("/Users/user/video/test_video.mp4")
        liss1[3].send_keys("/Users/user/video/322.jpg")
        practical_guide_page.add_files()
        time.sleep(1)
        #practical_guide_page.click_save_button()
        #time.sleep(10)
        practical_guide_page.click_back_to_list()
        practical_guide_page.click_yes()
        #practical_guide_page.click_hyprlink_button()
        #practical_guide_page.enter_hyper_link("test.com")
        #liss = self.driver.find_elements_by_css_selector("span.x-btn-inner.x-btn-inner-default-toolbar-small")
        #time.sleep(1)
        #liss[3].click()
        for li in liss:
            print (li.get_attribute('class'))

        practical_guide_page.enter_all_filter("all")
        practical_guide_page.click_just_created_practical_guide()
        practical_guide_page.click_deactivate()
        time.sleep(5)
        practical_guide_page.click_back_to_list()
        #practical_guide_page.click_yes()

        #DELETE PG
        practical_guide_page.enter_all_filter("all")
        practical_guide_page.click_created_practical_guide()
        practical_guide_page.click_dots_button()
        practical_guide_page.click_delete_practical_guide()
        #practical_guide_page.click_yes_to_delete()
        #CREATE COOKBOOK'''
    def test_cookbook_functionality(self):
        self.driver.get(self.base_url)
        login_page = page.LoginPage(self.driver)
        practical_guide_page = page.PracticalGuidePage(self.driver)
        forgot_password = page.ForgotPasswordFunctionality(self.driver)
        cookbook_page = page.CookBookPage(self.driver)
        asserts = page.AssertIDs(self.driver)

        #LOGIN
        login_page.input_email_sign_in("test@mev.com")
        login_page.input_password_field("12345678")
        time.sleep(0.3)
        login_page.click_login_button()
        #time.sleep(6)
        practical_guide_page.wait_until_practical_guide_opened()
        assert asserts.practical_guide_page_opened() in self.driver.page_source

        #GO TO COOKBOOK
        cookbook_page.click_cookbook()


        #Check category creation
        cookbook_page.click_category_overview()
        time.sleep(2)
        cookbook_page.click_new_to_create_categoty()
        cookbook_page.enter_category_name("piven")
        cookbook_page.enter_category_comment("top comment in the world")
        cookbook_page.click_save_category()
        time.sleep(3)

        #Check recipe creation with new category
        cookbook_page.click_overview_to_create_new_recipe()
        cookbook_page.click_cookbook_dots_button()
        time.sleep(2)
        cookbook_page.click_create_new_recipe()
        cookbook_page.enter_name("a test name")
        cookbook_page.enter_category("piven")
        cookbook_page.enter_time("30")
        cookbook_page.add_header_image("/Users/user/video/322.jpg")
        cookbook_page.add_featured_img("/Users/user/video/4396.jpg")
        cookbook_page.enter_description("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                        "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                        "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                        "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        cookbook_page.click_ingridients()
        cookbook_page.click_add_ingredient()
        cookbook_page.enter_ingredients_name("test01")
        cookbook_page.enter_ingredient_measurement("oz")
        cookbook_page.enter_ingredient_amount("7")
        cookbook_page.enter_ingredient_category("Dairy")

        cookbook_page.click_ingridients()
        cookbook_page.click_add_ingredient()
        cookbook_page.enter_ingredients_name("test02")
        cookbook_page.enter_ingredient_measurement_without_wait("tsp")
        cookbook_page.enter_ingredient_amount_without_wait("6")
        cookbook_page.enter_ingredient_category_without_wait("Protein")

        cookbook_page.click_ingridients()
        cookbook_page.click_add_ingredient()
        cookbook_page.enter_ingredients_name("test03")
        cookbook_page.enter_ingredient_measurement_without_wait("lbs")
        cookbook_page.enter_ingredient_amount_without_wait("0.5")
        cookbook_page.enter_ingredient_category_without_wait("Veggies")

        cookbook_page.click_ingridients()
        cookbook_page.click_add_ingredient()
        cookbook_page.enter_ingredients_name("test04")
        cookbook_page.enter_ingredient_measurement_without_wait("cup")
        cookbook_page.enter_ingredient_amount_without_wait("8")
        cookbook_page.enter_ingredient_category_without_wait("Fruit")

        cookbook_page.click_ingridients()
        cookbook_page.click_add_ingredient()
        cookbook_page.enter_ingredients_name("test05")
        cookbook_page.enter_ingredient_measurement_without_wait("bunch")
        cookbook_page.enter_ingredient_amount_without_wait("9")
        cookbook_page.enter_ingredient_category_without_wait("Grains")

        cookbook_page.click_preparation()
        cookbook_page.click_add_step()
        cookbook_page.enter_preparation_text("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                             "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        cookbook_page.click_preparation()
        cookbook_page.click_add_step()
        cookbook_page.enter_preparation_text("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                             "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        cookbook_page.click_preparation()
        cookbook_page.click_add_step()
        cookbook_page.enter_preparation_text("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                             "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        cookbook_page.click_preparation()
        cookbook_page.click_add_step()
        cookbook_page.enter_preparation_text("Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
                                             "Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor ")
        cookbook_page.click_preparation()
        cookbook_page.click_activate_recipe()
        cookbook_page.click_back_to_all_recipes()
        cookbook_page.yes_save_changes()
        time.sleep(10)
        cookbook_page.click_name_filter()
        cookbook_page.click_created_recipe()
        cookbook_page.click_cookbook_dots_button()
        cookbook_page.click_deactivate_recipe()
        time.sleep(5)
        cookbook_page.click_created_recipe()
        cookbook_page.click_cookbook_dots_button()
        cookbook_page.click_delete_recipe()
        #cookbook_page.yes_save_changes()
        '''time.sleep(2)

        #Check filters (cookbook)
        cookbook_page.click_name_filter()
        cookbook_page.click_name_filter()
        cookbook_page.click_status_filter()
        cookbook_page.click_status_filter()
        cookbook_page.click_date_created_filter()
        cookbook_page.click_date_created_filter()
        cookbook_page.click_last_updated_filter()
        cookbook_page.click_last_updated_filter()'''





    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    HTMLTestRunner.main()











