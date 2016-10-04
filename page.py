from selenium.common.exceptions import NoSuchElementException
from locators import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.exeption = NoSuchElementException


class LoginPage(BasePage):

    def input_email_sign_in(self, param1):
        email_field = self.driver.find_element(*SignInLocators.EMAIL_FIELD)
        email_field.send_keys(param1)


    def input_password_field(self, param1):
        input_pass = self.driver.find_element(*SignInLocators.PASSWORD_FIELD)
        input_pass.send_keys(param1)

    def click_login_button(self):
        click_login = self.driver.find_element(*SignInLocators.LOGIN_BUTTON)
        click_login.click()

    def wait_until_ok_is_present(self):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(((By.XPATH, ".//*[@id='button-1005']")))
            )
        finally:
            pass
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='button-1005']")))
        #element2 = self.driver.find_element(*SignInLocators.OK_BUTTON)
        #element2.click()

    def click_ok_button(self):
        ok_button = self.driver.find_element(*SignInLocators.OK_BUTTON)
        ok_button.click()

    def clear_email_sign_in(self):
        email_field_clear = self.driver.find_element(*SignInLocators.EMAIL_FIELD)
        email_field_clear.clear()

    def clear_password_field(self):
        clear_pass = self.driver.find_element(*SignInLocators.PASSWORD_FIELD)
        clear_pass.clear()


class ForgotPasswordFunctionality(BasePage):
    def click_forgot_password(self):
        click_forgot = self.driver.find_element(*SignInLocators.FORGOT_PASSWORD_BUTTON)
        click_forgot.click()

    def open_gmail_in_new_tab(self):
        elem = self.driver.find_element(*SignInLocators.FORGOT_PASSWORD_BUTTON)
        elem.send_keys(Keys.COMMAND + 't')
        self.driver.get("https://mail.google.com")

    def enter_email_gmail(self, param1):
        email_login = self.driver.find_element(*GmailLocators.GMAIL_EMAIL)
        email_login.send_keys(param1)

    def enter_email_pwd(self, param1):
        email_pwd = self.driver.find_element(*GmailLocators.GMAIL_PWD)
        email_pwd.send_keys(param1)

    def click_next(self):
        next_button = self.driver.find_element(*GmailLocators.NEXT_BUTTON)
        next_button.click()

    def click_sign_in(self):
        sign_in = self.driver.find_element(*GmailLocators.SIGN_IN_BUTTON)
        sign_in.click()

    def click_correct_mail(self):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((GmailLocators.MAIL_ID))
            )
            element.click()
        finally:
            pass
            #click_mail = self.driver.find_element(*GmailLocators.MAIL_ID)
            #click_mail.click()

    def input_forgot_email(self, param1):
        input_forgot_email = self.driver.find_element(*ForgotPasswordLocators.INPUT_FIELD)
        input_forgot_email.send_keys(param1)

    def click_send_email(self):
        send_button = self.driver.find_element(*ForgotPasswordLocators.SEND_EMAIL_BUTTON)
        send_button.click()

    def click_go_to_admin(self):
        click_go_admin = self.driver.find_element(*ForgotPasswordLocators.GO_TO_ADMIN_BUTTON)
        click_go_admin.click()

    def click_reset_password_mail(self):
        click_reset = self.driver.find_element(*GmailLocators.RESET_PWD_MAIL)
        click_reset.click()

    def input_new_pwd(self, param1):
        input_new_pwd = self.driver.find_element(*ForgotPasswordLocators.NEW_PWD_FIELD)
        input_new_pwd.send_keys(param1)

    def input_confitm_pwd(self, param1):
        input_confirm = self.driver.find_element(*ForgotPasswordLocators.CONFIRM_PWD_FIELD)
        input_confirm.send_keys(param1)

    def clear_new_pwd(self):
        clear_field = self.driver.find_element(*ForgotPasswordLocators.NEW_PWD_FIELD)
        clear_field.clear()

    def clear_confirm_pwd(self):
        clear_field = self.driver.find_element(*ForgotPasswordLocators.CONFIRM_PWD_FIELD)
        clear_field.clear()

    def click_reset_your_password(self):
        click_reset_pwd = self.driver.find_element(*ForgotPasswordLocators.RESET_PWD_BUTTON)
        click_reset_pwd.click()

class PracticalGuidePage(BasePage):

    def click_logout(self):
        click_logout_button = self.driver.find_element(*PracticalGuideLocators.LOGOUT_BUTTON)
        click_logout_button.click()

    def click_burger(self):
        click_burger = self.driver.find_element(*PracticalGuideLocators.BURGER_ID)
        click_burger.click()

    def click_dots_button(self):
        click_dots = self.driver.find_element(*PracticalGuideLocators.DOTS_BUTTON)
        click_dots.click()

    def click_create_new_guide(self):
        click_add_guide = self.driver.find_element(*PracticalGuideLocators.CREATE_NEW_GUIDE)
        click_add_guide.click()

    def upload_video(self, video_path):
        upload_video = self.driver.find_element(*PracticalGuideLocators.UPLOAD_VIDEO_BUTTON_ID)
        upload_video.send_keys(video_path)

    def input_name(self, name):
        input_name = self.driver.find_elements(*PracticalGuideLocators.NAME_FIELD_ID)
        input_name[2].send_keys(name)

    def input_categories(self, categoty):
        input_cat = self.driver.find_element(*PracticalGuideLocators.CATEGORIES_FIELD_ID)
        input_cat.send_keys(categoty)

    def input_author(self, author):
        click_label = self.driver.find_elements(*PracticalGuideLocators.LABEL_AUTHOR_ID)
        click_label[7].click()
        click_label[7].click()
        input_author = self.driver.find_element(*PracticalGuideLocators.AUTHOR_FIELD_ID)
        input_author.send_keys(author)

    def click_save_button(self):
        click_save = self.driver.find_element(*PracticalGuideLocators.SAVE_BUTTON_ID)
        click_save.click()

    def upload_featured_img(self, path):
        click_upload = self.driver.find_elements(*PracticalGuideLocators.UPLOAD_VIDEO_BUTTON_ID)
        click_upload[1].send_keys(path)

    def input_featured_text(self, text):
        input_text = self.driver.find_element(*PracticalGuideLocators.FEATURED_TEXT_FIELD_ID)
        input_text.send_keys(text)

    def click_activate(self):
        click_activate = self.driver.find_elements(*PracticalGuideLocators.ACTIVATE_BUTTON_ID)
        click_activate[0].click()

    def enter_text_guide(self, text):
        enter_text = self.driver.find_element(*PracticalGuideLocators.ENTER_INFO_GUIDE_ID)
        enter_text.send_keys(text)

    def highlight_all(self):
        highlight = self.driver.find_element(*PracticalGuideLocators.ENTER_INFO_GUIDE_ID)
        highlight.send_keys(Keys.COMMAND+'a')

    def click_numbers(self):
        click_numbers = self.driver.find_element(*PracticalGuideLocators.NUMBERS_ID)
        click_numbers.click()

    def click_dots(self):
        click_dots = self.driver.find_element(*PracticalGuideLocators.DOTS_ID)
        click_dots.click()

    def click_header_one(self):
        click_header = self.driver.find_element(*PracticalGuideLocators.HEADER1_ID)
        click_header.click()

    def click_header_two(self):
        click_header = self.driver.find_element(*PracticalGuideLocators.HEADER2_ID)
        click_header.click()

    def clear_filters(self):
        clear = self.driver.find_element(*PracticalGuideLocators.CLEAR_FILTERS_ID)
        clear.click()

    def click_wysywyg(self):
        click = self.driver.find_element(*PracticalGuideLocators.ENTER_INFO_GUIDE_ID)
        click.click()

    def upload_new_video(self):
        upload = self.driver.find_element(*PracticalGuideLocators.EDITOR_VIDEO_ID)
        upload.click()

    def choose_file(self, path):
        choose_file = self.driver.find_element(*PracticalGuideLocators.CHOOSE_FILE_ID)
        choose_file.send_keys(path)

    def add_files(self):
        add = self.driver.find_element(*PracticalGuideLocators.UPLOAD_ID)
        add.click()

    def click_hyprlink_button(self):
        hyperlink_button = self.driver.find_element(*PracticalGuideLocators.HYPERLINK_BUTTON_ID)
        #hyperlink_button.click()
        actionChains = ActionChains(self.driver)
        actionChains.double_click(hyperlink_button).perform()


    def enter_hyper_link(self, link):
        enter_link = self.driver.find_element(*PracticalGuideLocators.ENTER_LINK_ID)
        enter_link.send_keys(link)

    def click_mini_modal(self):
        click_modal = self.driver.find_element(*PracticalGuideLocators.MINI_MODAL_ID)
        click_modal.click()

    def enter_text_to_textarea(self, text):
        enter_text = self.driver.find_element(*PracticalGuideLocators.MINI_MODAL_TEXTAREA_ID)
        enter_text.send_keys(text)

    def click_back_to_list(self):
        elem1 = self.driver.find_elements(*PracticalGuideLocators.BACK_TO_LIST_ID)
        elem1[3].click()

    def wait_until_practical_guide_opened(self):
        '''elem = self.driver.find_elements(By.CLASS_NAME, "x-grid-item")
        elem[5].click()
        for li in elem:
            print (li.get_attribute('innerHTML'))'''
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, "x-grid-item")))
        finally:
            pass

    def wait_until_practical_guide_opened1(self):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((PracticalGuideLocators.SAVE_BUTTON_ID)))
        finally:
            pass

    def click_yes(self):
        elem = self.driver.find_elements(*PracticalGuideLocators.BACK_YES_ID)
        elem[3].click()
        for li in elem:
            print (li.get_attribute('class'))

    def enter_all_filter(self, quantity):
        elem = self.driver.find_elements(*PracticalGuideLocators.ALL_ID)
        elem[1].send_keys(quantity)
        time.sleep(1)
        elem[1].send_keys(Keys.ENTER)
        time.sleep(3)

    def click_just_created_practical_guide(self):
        element = self.driver.find_elements(*PracticalGuideLocators.NEW_PRACTICAL_GUIDE_ID)
        for li in element:
            print (li.get_attribute('class'))
        actionChains = ActionChains(self.driver)
        actionChains.double_click(element[124]).perform()

    def click_deactivate(self):
        element = self.driver.find_element(*PracticalGuideLocators.DEACTIVATE_BUTTON_ID)
        element.click()

    def click_delete_practical_guide(self):
        element = self.driver.find_element(*PracticalGuideLocators.DELETE_PRACTICAL_GUIDE)
        element.click()

    def click_yes_to_delete(self):
        element = self.driver.find_element(*LocatorsCookBook.YES_SAVE_CHANGES_ID)
        element.click()

    def click_created_practical_guide(self):
        element = self.driver.find_elements(*PracticalGuideLocators.NEW_PRACTICAL_GUIDE_ID)
        for li in element:
            print (li.get_attribute('class'))
        element[124].click()

class CookBookPage(BasePage):

    def click_cookbook(self):
        element = self.driver.find_elements(*LocatorsCookBook.COOKBOOK_ID)
        element[2].click()

    def click_cookbook_dots_button(self):
        click_dots = self.driver.find_elements(*LocatorsCookBook.COOKBOOK_DOTS_ID)
        click_dots[1].click()

    def click_create_new_recipe(self):
        click_add_recipe = self.driver.find_elements(*PracticalGuideLocators.CREATE_NEW_GUIDE)
        click_add_recipe[4].click()

    def enter_name(self, name):
        element = self.driver.find_elements(*PracticalGuideLocators.NAME_FIELD_ID)
        element[6].send_keys(name)

    def enter_category(self, category):
        element = self.driver.find_elements(*PracticalGuideLocators.CATEGORIES_FIELD_ID)
        element[3].send_keys(category)
        elem = self.driver.find_elements(*PracticalGuideLocators.CATEGORIES_FIELD_ID)
        elem[3].send_keys(Keys.ENTER)

    def enter_time(self, time):
        element = self.driver.find_elements(*LocatorsCookBook.TIME_ID)
        element[7].send_keys(time)

    def add_header_image(self, image_path):
        element = self.driver.find_elements(*PracticalGuideLocators.UPLOAD_VIDEO_BUTTON_ID)
        element[2].send_keys(image_path)

    def add_featured_img(self, image_path):
        element = self.driver.find_elements(*PracticalGuideLocators.UPLOAD_VIDEO_BUTTON_ID)
        element[3].send_keys(image_path)

    def enter_description(self, text):
        element = self.driver.find_elements(*LocatorsCookBook.DESCRIPTION_ID)
        for li in element:
            print (li.get_attribute('class'))
        element[1].send_keys(text)

    def click_ingridients(self):
        element = self.driver.find_elements(*LocatorsCookBook.INGRIDIENTS_ID)
        element[14].click()

    def click_add_ingredient(self):
        element = self.driver.find_elements(*LocatorsCookBook.ADD_INGRIDIENT_ID)
        element[1].click()
        '''try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((LocatorsCookBook.ADD_INGRIDIENT_ID))
            )
            element.click()
        finally:
            pass'''

    def enter_ingredient_name(self, name):
        element = self.driver.find_elements(*LocatorsCookBook.INGREDIENT_NAME)
        element[1].send_keys(name)
        element.send_keys(Keys.TAB)

    def enter_ingredient_measurement(self, measurement):
        element = self.driver.find_element(*LocatorsCookBook.MEASUREMENT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        time.sleep(2)
        element.send_keys(measurement)
        element.send_keys(Keys.TAB)

    def enter_ingredient_measurement_without_wait(self, measurement):
        element = self.driver.find_element(*LocatorsCookBook.MEASUREMENT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        element.send_keys(measurement)
        element.send_keys(Keys.TAB)

    def enter_ingredient_amount(self, amount):
        element = self.driver.find_element(*LocatorsCookBook.AMOUNT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        time.sleep(2)
        element.send_keys(amount)
        element.send_keys(Keys.TAB)

    def enter_ingredient_amount_without_wait(self, amount):
        element = self.driver.find_element(*LocatorsCookBook.AMOUNT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        element.send_keys(amount)
        element.send_keys(Keys.TAB)

    def enter_ingredient_category(self, category):
        element = self.driver.find_element(*LocatorsCookBook.CATEGORY_INGREDIENT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        time.sleep(2)
        element.send_keys(category)

    def enter_ingredient_category_without_wait(self, category):
        element = self.driver.find_element(*LocatorsCookBook.CATEGORY_INGREDIENT_ID)
        element2 = self.driver.find_element(*LocatorsCookBook.ARROW_DOWN_ID)
        element2.click()
        element.send_keys(category)

    def click_preparation(self):
        element = self.driver.find_elements(*LocatorsCookBook.INGRIDIENTS_ID)
        element[15].click()

    def enter_preparation_text(self, text):
        element = self.driver.find_element(*LocatorsCookBook.PREPARATION_TEXTAREA_ID)
        element.send_keys(text)

    def click_add_step(self):
        element = self.driver.find_elements(*LocatorsCookBook.ADD_STEP_ID)
        element[2].click()

    def click_activate_recipe(self):
        click_activate = self.driver.find_elements(*PracticalGuideLocators.ACTIVATE_BUTTON_ID)
        click_activate[2].click()

    def click_back_to_all_recipes(self):
        elem1 = self.driver.find_elements(*PracticalGuideLocators.BACK_TO_LIST_ID)
        elem1[13].click()

    def yes_save_changes(self):
        element = self.driver.find_element(*LocatorsCookBook.YES_SAVE_CHANGES_ID)
        element.click()

    def click_created_recipe(self):
        element = self.driver.find_element(*LocatorsCookBook.PIVEN_ID)
        #for li in element:
            #print (li.get_attribute('innerHTML'))
        time.sleep(2)
        element.click()

    def click_deactivate_recipe(self):
        element = self.driver.find_elements(*LocatorsCookBook.DEACTIVATE_ID)
        element[1].click()

    def click_delete_recipe(self):
        element = self.driver.find_elements(*LocatorsCookBook.DELETE_ID)
        element[1].click()

    def enter_ingredients_name(self, name):
        elem = self.driver.find_elements(*LocatorsCookBook.INGREDIENT_NAME)
        try:
            elem2 = self.driver.find_elements(*LocatorsCookBook.INGREDIENT_NAME_ACTIVE)
            elem2[6].send_keys(name)
            elem2[6].send_keys(Keys.TAB)
        except self.exeption:
            elem[6].send_keys(name)
            elem[6].send_keys(Keys.TAB)

    def click_name_filter(self):
        element = self.driver.find_elements(*LocatorsCookBook.FILTERS_LOCATOR_ID)
        element[12].click()
        time.sleep(2)

    def click_status_filter(self):
        element = self.driver.find_elements(*LocatorsCookBook.FILTERS_LOCATOR_ID)
        element[13].click()
        time.sleep(2)

    def click_date_created_filter(self):
        element = self.driver.find_elements(*LocatorsCookBook.FILTERS_LOCATOR_ID)
        element[15].click()
        time.sleep(2)

    def click_last_updated_filter(self):
        element = self.driver.find_elements(*LocatorsCookBook.FILTERS_LOCATOR_ID)
        element[16].click()
        time.sleep(2)

    def click_category_overview(self):
        element = self.driver.find_elements(*LocatorsCookBook.CATEGORY_OVERVIEW_ID)
        element[12].click()

    def click_new_to_create_categoty(self):
        element = self.driver.find_element(*LocatorsCookBook.NEW_CATEGORY_ID)
        element.click()

    def enter_category_name(self, name):
        element = self.driver.find_element(*LocatorsCookBook.CATEGORY_NAME_FIELD_ID)
        element.send_keys(name)
        element.send_keys(Keys.TAB)

    def enter_category_comment(self, comment):
        element = self.driver.find_element(*LocatorsCookBook.COMMENTS_FIELD_ID)
        element.send_keys(comment)

    def click_save_category(self):
        element = self.driver.find_elements(*LocatorsCookBook.SAVE_CATEGORY_ID)
        element[1].click()

    def click_overview_to_create_new_recipe(self):
        element = self.driver.find_elements(*LocatorsCookBook.CATEGORY_OVERVIEW_ID)
        element[11].click()


class AssertIDs(BasePage):
    def login_page_title(self):
        return  AssertTitles.SIGN_IN_TITLE

    def validation_error(self):
        return AssertTitles.INVALID_EMAIL_PASSWORD

    def not_active_admin_error(self):
        return AssertTitles.ADMIN_NOT_ACTIVE

    def practical_guide_page_opened(self):
        return AssertTitles.PRACTICAL_GUIDE_OPENED

