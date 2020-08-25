import pandas as pd
from selenium import webdriver
from collections import OrderedDict
from time import sleep
#from bs4 import BeautifulSoup as BS
def plate_history(plate_no):
    url="https://vehiclehistory.in/"
    #driver path
    browser = webdriver.Firefox(executable_path="/home/vikram/anaconda3/geckodriver")
    browser.get(url)

    vehicle_reg_no  = browser.find_element_by_xpath('//*[@id="vehicle_reg_no"]')
    vehicle_reg_no .send_keys(plate_no)
    get_result = browser.find_element_by_xpath('//*[@id="submit_history"]')
    get_result.click()
    sleep(2)
    browser.quit()
    return ('ok hare krishna');