from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from test_locators import locators
from test_data import data
from selenium.webdriver.support.wait import WebDriverWait
# Python Expected Conditions
from selenium.webdriver.support import expected_conditions as EC
# Python Selenium Exception
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pytest

class Sana:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def __init__(self) -> None:
        self.driver.get(data.Sana_Data().url)
        self.driver.maximize_window()

    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Sana_Locators().username_inputBox).send_keys(data.Sana_Data().username)    
        self.driver.find_element(by=By.NAME, value=locators.Sana_Locators().password_InputBox).send_keys(data.Sana_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Sana_Locators().LoginButton).click()
        sleep(5)

    def invalid_login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Sana_Locators().username_inputBox).send_keys(data.Sana_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Sana_Locators().password_InputBox2).send_keys(data.Sana_Data().password2)
        self.driver.find_element(by=By.XPATH, value=locators.Sana_Locators().LoginButton).click()
        sleep(5)



    def add_employee(self):
        sleep(10)  
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)
        
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        action = ActionChains(self.driver)                    
        sleep(10)
        action.click(source).perform()
        sleep(20)
    
        source = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        action = ActionChains(self.driver)
        sleep(10)
        action.click(on_element=source)
        action.send_keys("sana")
        sleep(5)
        action.perform()
        sleep(5)

        source = self.driver.find_element(by=By.NAME, value='middleName')
        action = ActionChains(self.driver)
        sleep(10)
        action.click(on_element=source)
        action.send_keys("sumayya")
        sleep(5)
        action.perform()
        sleep(5)

        source = self.driver.find_element(by=By.NAME, value='lastName')
        action = ActionChains(self.driver)
        sleep(10)
        action.click(on_element=source)
        action.send_keys("ahmed")
        sleep(5)
        action.perform()
        sleep(5)

        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20) 

    def edit_employee(self):
        sleep(10)  
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)
        
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)

        source = self.driver.find_element(by=By.NAME, value='firstName')
        action = ActionChains(self.driver)
        sleep(10)
        action.click(on_element=source)
        action.send_keys("alia")
        sleep(5)
        action.perform()
        sleep(5)                 

        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)

    def delete_employee(self):
        sleep(10)  
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)
        
        sleep(10) 
        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[1]/i')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)

        source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]/i')
        action = ActionChains(self.driver)
        sleep(10) 
        action.click(source).perform()
        sleep(20)      


Sana().login()
# Sana().invalid_login()
#Sana().add_employee()
# Sana().edit_employee()
# Sana().delete_employee()