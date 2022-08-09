from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(r"C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

driver.maximize_window()

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name_form = driver.find_element(by=By.NAME, value="fName")
l_name_form = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
send_button = driver.find_element(by=By.CLASS_NAME, value="btn")

f_name_form.send_keys("Libor")
l_name_form.send_keys("Havranek")
email.send_keys("liborhavranek@gmail.com")

send_button.click()
