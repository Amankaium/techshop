from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
from time import sleep


class HomepageTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get("/")

    # def tearDown(self):
    def test_redirect_from_homepage_302_success(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response.url, reverse("products"))

    def test_open_homepage_200_fail(self):
        self.assertNotEqual(self.response.status_code, 200)


class AuthTestCase(TestCase):
    def test_load_auth_page_success(self):
        driver = webdriver.Chrome()
        driver.get("localhost:8000/")

        # driver.find_element_by_xpath("//a[@href='/login/']").click()
        driver.find_element_by_xpath("//a[contains(@href, 'login')]").click()
        
        # assert "form" in driver.page_source
        self.assertIn("form", driver.page_source)
        # sleep(3)
        driver.close()
