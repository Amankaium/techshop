from django.test import TestCase
from selenium import webdriver
from time import sleep
from .models import FeedBack


class FeedBackTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.close()
        # fb = FeedBack.objects.last()
        # fb.delete()

    def test_add_form_success(self):
        self.driver.get("http://localhost:8000")
        sleep(3)
    
        name = self.driver.find_element_by_id("id_name")
        name.send_keys("Jeff Bezos")

        text = self.driver.find_element_by_id("id_text")
        text.send_keys("Amazon is better!")

        text = self.driver.find_element_by_id("id_phone")
        text.send_keys("+12-351-3613-(12312)")

        text = self.driver.find_element_by_id("id_email")
        text.send_keys("testblabla@gmail.com")

        self.driver.find_element_by_xpath("//*[contains(text(), 'Отправить')]").click()
    
    def test_form_max_length(self):
        self.driver.get("http://localhost:8000/product/all/")

        test_str = "a" * 257

        name = self.driver.find_element_by_id("id_name")
        name.send_keys(test_str)
        self.assertNotEqual(test_str, name.get_attribute("value"))

        phone = self.driver.find_element_by_id("id_phone")
        phone.send_keys(test_str)
        self.assertNotEqual(test_str, phone.get_attribute("value"))

        email = self.driver.find_element_by_id("id_email")
        email.send_keys(test_str)
        self.assertNotEqual(test_str, email.get_attribute("value"))



    
        

