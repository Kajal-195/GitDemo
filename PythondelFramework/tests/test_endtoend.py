import self as self
from selenium import webdriver
import time
import pytest

from Baseclass import BaseClass


class Testone(BaseClass):

    def test_end2end(self):

        self.driver.find_element_by_css_selector("a[href='shop']").click()
        cards= self.driver.find_elements_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i= i+1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                self.driver.find_elements_by_css_selector(".card-footer button")[i].click()

        self.driver.find_elements_by_css_selector("a[class*='btn-primary']").click()

        self.driver.find_elements_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")