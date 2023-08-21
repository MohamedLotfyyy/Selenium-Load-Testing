from selenium import webdriver
import os
import sales_package.constant as const
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker

class odooTest(webdriver.Chrome):

    def __init__(self, driver_path='/Users/mohamedlotfy/Documents/SeleniumDriver', close = False):

        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(odooTest, self).__init__(options=options)

        self.close = close
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Code to clean up the resource
        if(self.close):
            self.quit()  # Close the browser window

    def first_landing_page(self):
        self.get(const.page_url)  # Open the landing page using the Selenium WebDriver
    
    def enter_email_pass(self):
        email_input = self.find_element(By.ID, 'login')
        email_input.send_keys("admin")
        pass_input = self.find_element(By.ID, 'password')
        pass_input.send_keys("admin")
        login_btn = self.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
        login_btn.click()
    
    def sales_section(self):
        toggle_btn = self.find_element(By.CSS_SELECTOR, 'button[class="dropdown-toggle"]')
        toggle_btn.click()
        sales_section = self.find_element(By.CSS_SELECTOR, 'a[data-menu-xmlid="sale.sale_menu_root"]')
        sales_section.click()
        self.implicitly_wait(20)
        create_new_btn = self.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary o_list_button_add"]')
        create_new_btn.click()

    def new_order(self):
        fake = Faker()
        first_name = fake.first_name()
        name_input = self.find_element(By.ID, 'partner_id')
        name_input.send_keys(first_name)
        self.implicitly_wait(20)
        create_name = self.find_element(By.CSS_SELECTOR, 'li[class="o-autocomplete--dropdown-item ui-menu-item o_m2o_dropdown_option o_m2o_dropdown_option_create"]')
        create_name.click()
        name_input.send_keys(Keys.ENTER)
        self.implicitly_wait(20)
        add_product = self.find_elements(By.CSS_SELECTOR, 'a[role="button"]')
        for button in add_product:
            if(button.text == 'Add a product'):
                button.click()
        product_input = self.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
        print(product_input)
        product_input[5].send_keys("desk")
        product_input[5].send_keys(Keys.ENTER)
        confirm_product = self.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary o_sale_product_configurator_edit"]')
        confirm_product.click()
        for i in range(100):
            message_btn = self.find_element(By.CSS_SELECTOR, 'button[class="o_ChatterTopbar_button o_ChatterTopbar_buttonSendMessage btn text-nowrap me-2 btn-odoo"]')
            message_btn.click()
            message_input = self.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Send a message to followers..."]')
            message_input.send_keys("hello mate")
            self.implicitly_wait(20)
            send_message = self.find_element(By.CSS_SELECTOR, 'button[class="o_Composer_actionButton o_Composer_button o_Composer_buttonSend btn btn-primary o-last o-has-current-partner-avatar"]')
            send_message.click()
        self.implicitly_wait(20)

     
        


        