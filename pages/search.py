"""
This module contains BookMyShowHomePage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BookMyShowHomePage:
  #URL
  URL = 'https://in.bookmyshow.com/'
  
  #Locators
  WRZK_ALERT = (By.CLASS_NAME,"div.wzrk-alert")
  CANCEL_BUTTON = (By.XPATH,'//button[@id="wzrk-cancel"]')
  SEARCH_INPUT = (By.XPATH, '//input[@type="text" and contains(@placeholder,"city")]')
  ALL_CITIES = (By.CLASS_NAME,'hSXkgd')
  OTHER_CITIES = (By.XPATH, '//span[contains(.,"Other Cities")]')
  SEARCH_RESULTS = (By.XPATH, '//span[contains(@class,"dQiAET")]')
  NO_RESULTS = (By.XPATH, '//span[contains(.,"No Results found")]')

  #Initializer
  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def closeAlert(self):
    alert = self.browser.find_element(*self.CANCEL_BUTTON)
    alert.click()

  def selectCity(self, city):
    CITY_ICON = (By.XPATH, f'//div[contains(@class,"dXjdGj")][contains(.,"{city}")]')
    mumbai = self.browser.find_element(*CITY_ICON)
    mumbai.click()

  def clickAllCities(self):
    all_cities = self.browser.find_element(*self.ALL_CITIES)
    all_cities.click()

  def search(self, city):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(city)
    search_input.click()

  def findOtherCities(self):
    other_cities = self.browser.find_element(*self.OTHER_CITIES)
    return other_cities
  
  def getSearchList(self):
    city_list = self.browser.find_elements(*self.SEARCH_RESULTS)
    no_results = self.browser.find_elements(*self.NO_RESULTS)
    if(city_list):  
      cities = [city.text for city in city_list]
      return cities 
    else:
      result = [city.text for city in no_results]
      return result

  def searchSelectCity(self, city):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(city + Keys.RETURN)
