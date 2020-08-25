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

        self.driver.find_element_by_xpath("//*[contains(text(), 'Отправить')]").click()

    
        

