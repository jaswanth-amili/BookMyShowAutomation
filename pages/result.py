"""
This module contains BookMyShowResultPage,
the page object for the DuckDuckGo search result page.
"""
import time

from selenium.webdriver.common.by import By

class BookMyShowResultPage:
  RESULT_LINKS = (By.CSS_SELECTOR, 'div.iYtpgd')
  CITY_DROPDOWN = (By.XPATH, '//span[contains(@class,"ellipsis")]')
  ALL_CITIES = (By.CLASS_NAME,'hSXkgd')

  def __init__(self, browser):
    self.browser = browser

  def getCardText(self):
    self.browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    self.browser.execute_script("window.scrollTo(0,-200)")
    return titles
  
  def clickCityDropdown(self):
    city_dropdown = self.browser.find_element(*self.CITY_DROPDOWN)
    city_dropdown.click()

  