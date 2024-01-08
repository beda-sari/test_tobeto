# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBosbirakma():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bosbirakma(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
    email = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
    email.click()
    password = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
    password.click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
    self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/p[1]")))
    assert self.driver.find_element(By.XPATH, "//*[@id=\'__next\']/div/main/section/div/div/div/div/form/p[1]").text == "Doldurulması zorunlu alan*"
    WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\'__next\']/div/main/section/div/div/div/div/form/p[2]")))
    assert self.driver.find_element(By.XPATH, "//*[@id=\'__next\']/div/main/section/div/div/div/div/form/p[2]").text == "Doldurulması zorunlu alan*"
    
  