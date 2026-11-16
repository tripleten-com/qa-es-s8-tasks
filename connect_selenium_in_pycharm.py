from selenium import webdriver
import time

# Inicializa el driver
driver = webdriver.Chrome()

# Agrega una espera
time.sleep(5)

# Cierra el navegador
driver.quit()
