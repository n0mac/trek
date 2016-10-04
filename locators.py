from selenium.webdriver.common.by import By

class SignInLocators(object):
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "passwordPlain")
    LOGIN_BUTTON = (By.XPATH, ".//*[@id='button-1017-btnEl']")
    OK_BUTTON = (By.LINK_TEXT, "OK")
    OK_BUTTON_NEGATIVE = (By.XPATH, "Oh_no")
    FORGOT_PASSWORD_BUTTON = (By.LINK_TEXT, "Forgot Password?")

class PracticalGuideLocators(object):
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    BURGER_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-default-toolbar-small.icon-icons_Menu")
    DOTS_BUTTON = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-default-toolbar-small.icon-icons_More")
    CREATE_NEW_GUIDE = (By.CSS_SELECTOR, "span.x-menu-item-text.x-menu-item-text-default.x-menu-item-indent-no-separator")
    UPLOAD_VIDEO_BUTTON_ID = (By.CLASS_NAME, "x-form-file-input")
    NAME_FIELD_ID = (By.XPATH, ".//*[@class='x-form-field x-form-required-field x-form-text x-form-text-default  ']")
    CATEGORIES_FIELD_ID = (By.CLASS_NAME, "x-tagfield-input-field ")
    SAVE_BUTTON_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-bluebutton-medium")
    LABEL_AUTHOR_ID = (By.CSS_SELECTOR, "span.x-form-item-label-inner.x-form-item-label-inner-default")
    AUTHOR_FIELD_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    FEATURED_TEXT_FIELD_ID = (By.CSS_SELECTOR, "textarea.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-textarea")
    ACTIVATE_BUTTON_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-default-toolbar-small.icon-icons_Active ")
    ENTER_INFO_GUIDE_ID = (By.CLASS_NAME, "x-htmleditor-iframe")
    NUMBERS_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.icon-icons_NumberList ")
    DOTS_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.icon-icons_BulletList ")
    HEADER1_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.editorHeader1 ")
    HEADER2_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.editorHeader2 ")
    CLEAR_FILTERS_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.editorClearTextFontSize ")
    EDITOR_VIDEO_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.editorVideo")
    CHOOSE_FILE_ID = (By.CLASS_NAME, "x-form-file-input")
    UPLOAD_ID = (By.CSS_SELECTOR, "span.x-btn-button.x-btn-button-greenbutton-medium.x-btn-text.x-btn-button-center")
    HYPERLINK_BUTTON_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.icon-icons_URL ")
    ENTER_LINK_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    OK_BUTTON_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-default-small")
    MINI_MODAL_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-plain-toolbar-small.editorModal ")
    MINI_MODAL_TEXTAREA_ID = (By.CSS_SELECTOR, "textarea.x-form-field.x-form-text.x-form-text-default.x-form-textarea.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    BACK_TO_LIST_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-default-toolbar-small")
    BACK_YES_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-default-small")
    ALL_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default ")
    NEW_PRACTICAL_GUIDE_ID = (By.CSS_SELECTOR, "div.x-grid-cell-inner")
    DEACTIVATE_BUTTON_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-default-toolbar-small.icon-icons_Deactive ")
    DELETE_PRACTICAL_GUIDE = (By.CSS_SELECTOR, "div.x-menu-item-icon-default.x-menu-item-icon.icon-icons_Close-Delete ")

class AssertTitles(object):
    SIGN_IN_TITLE = "Sign In"
    INVALID_EMAIL_PASSWORD = "Invalid email or password"
    ADMIN_NOT_ACTIVE = "Admin is not active"
    PRACTICAL_GUIDE_OPENED = "Practical Guide"

class GmailLocators(object):
    GMAIL_EMAIL = (By.NAME, "Email")
    GMAIL_PWD = (By.NAME, "Passwd")
    NEXT_BUTTON = (By.ID, "next")
    SIGN_IN_BUTTON = (By.ID, "signIn")
    MAIL_ID = (By.XPATH, "//div [@class='y6']/span[contains(.,'Mountain Trek Password Recovery')]")
    RESET_PWD_MAIL = (By.LINK_TEXT, "Reset password")


class ForgotPasswordLocators(object):
    SEND_EMAIL_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/div/input")
    INPUT_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input")
    GO_TO_ADMIN_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/a")
    NEW_PWD_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input[1]")
    CONFIRM_PWD_FIELD = (By.XPATH, "html/body/div/div/div/div/div/form/input[2]")
    RESET_PWD_BUTTON = (By.XPATH, "html/body/div/div/div/div/div/form/div/input")

class LocatorsCookBook(object):
    COOKBOOK_ID = (By.CSS_SELECTOR, "span.x-tab-inner.x-tab-inner-default")
    COOKBOOK_DOTS_ID = (By.CSS_SELECTOR, "span.x-btn-icon-el.x-btn-icon-el-default-toolbar-small.icon-icons_More ")
    TIME_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default ")
    TIME_LABEL_ID = (By.CSS_SELECTOR, "span.x-form-item-label-inner.x-form-item-label-inner-default")
    DESCRIPTION_ID = (By.CSS_SELECTOR, "textarea.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-textarea")
    INGRIDIENTS_ID = (By.CSS_SELECTOR, "span.x-tab-inner.x-tab-inner-default")
    ADD_INGRIDIENT_ID = (By.CSS_SELECTOR, "span.x-btn-button.x-btn-button-greenbutton-medium.x-btn-text.x-btn-button-center ")
    INGREDIENT_NAME = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    MEASUREMENT_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    AMOUNT_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    CATEGORY_INGREDIENT_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    ARROW_DOWN_ID = (By.CSS_SELECTOR, "div.x-form-trigger.x-form-trigger-default.x-form-arrow-trigger.x-form-arrow-trigger-default.x-form-trigger-focus")
    PREPARATION_TEXTAREA_ID = (By.CSS_SELECTOR, "textarea.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-textarea.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    ADD_STEP_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-greenbutton-medium")
    YES_SAVE_CHANGES_ID = (By.XPATH, ".//*[@id='button-1006']")
    DEACTIVATE_ID = (By.CSS_SELECTOR, "div.x-menu-item-icon-default.x-menu-item-icon.icon-icons_Deactive ")
    INGREDIENT_NAME_ACTIVE = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default  ")
    DELETE_ID = (By.CSS_SELECTOR, "div.x-menu-item-icon-default.x-menu-item-icon.icon-icons_Close-Delete ")
    FILTERS_LOCATOR_ID = (By.CSS_SELECTOR, "span.x-column-header-text")
    CATEGORY_NAME_FIELD_ID = (By.CSS_SELECTOR, "input.x-form-field.x-form-required-field.x-form-text.x-form-text-default.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    NEW_CATEGORY_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-greenbutton-medium")
    CATEGORY_OVERVIEW_ID = (By.CSS_SELECTOR, "span.x-tab-inner.x-tab-inner-default")
    COMMENTS_FIELD_ID = (By.CSS_SELECTOR, "textarea.x-form-field.x-form-text.x-form-text-default.x-form-textarea.x-form-focus.x-field-form-focus.x-field-default-form-focus")
    SAVE_CATEGORY_ID = (By.CSS_SELECTOR, "span.x-btn-inner.x-btn-inner-bluebutton-medium")
    PIVEN_ID = (By.LINK_TEXT, "piven")




