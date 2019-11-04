
"""
Real website data scrapping for Kerela Results
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"



#browser = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
browser = webdriver.Firefox(executable_path="/home/vikram/anaconda3/geckodriver")
browser.get(url)


sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()

