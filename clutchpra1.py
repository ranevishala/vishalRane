from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class CompanyInfo:


    def __init__(self,con):
        self.contact=con

driver = webdriver.Chrome('E:\\chromedriver.exe')
driver.get('https://clutch.co/agencies?page=3')
companyList=driver.find_element_by_class_name('directory-list').find_elements_by_class_name('provider-row')

print('total Companies', len(companyList))

for index,company in enumerate(companyList):
    action = ActionChains(driver)
    action.move_to_element(company.find_element_by_class_name('nav').find_element_by_class_name('contact').click())

    time.sleep(1)
    print(company.find_element_by_tag_name('a').text) 
    
    # ithparynat pohochto aahe aata pan contact information print nahi karta yet aahe. 
    #<a id="KtGhkevAy" rel="nofollow" href="mailto:paul@gigantevaz.com">paul@gigantevaz.com</a>
    
    #  ya varil line madhe rel kay ahe??? means tag name tar nahiye. mag as name consider karu shakto ka?
