"""
These tests cover BookMyShow city search.
"""
import pytest
import time

from pages.result import BookMyShowResultPage
from pages.search import BookMyShowHomePage


# Select Mumbai and Verify displayed content
def test_select_mumbai(browser):
  search_page = BookMyShowHomePage(browser)
  result_page = BookMyShowResultPage(browser)
  city = 'Mumbai'
  
  # Given the BookMyShow city page is displayed
  search_page.load()
  time.sleep(0.1)
  search_page.closeAlert()    # Close customize alert

  # When the user selects "Mumbai"
  search_page.selectCity(city)
  
  # Then search result content pertain to "Mumbai"
  titles = result_page.getCardText()
  matches = [t for t in titles if city.lower() in t.lower()]
  assert len(matches) > 0

  # Click view all cities
  result_page.clickCityDropdown()
  search_page.clickAllCities()
  assert len(search_page.findOtherCities().text)>0
  
  # Enter Incorrect text and verify  no matching result display
  city = "abc"
  search_page.search(city)
  cities = search_page.getSearchList()
  assert (len(cities)==1 and cities[0]=='No Results found')
  # Enter the text "Co" and verify that all the matching cities of the entered letters is displayed
  city = "co"
  search_page.search(city)
  cities = search_page.getSearchList()
  results = [c for c in cities if city.lower() in c.lower()]
  assert len(results)>0

  # Select the city "Coimbatore" and verify the result page
  city = "Coimbatore"
  search_page.searchSelectCity(city)
  cardContent = result_page.getCardText()
  matches = [d for d in cardContent if city.lower() in d.lower()]
  assert len(matches) > 0