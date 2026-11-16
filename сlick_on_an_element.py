import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Inicializa una nueva instancia de Chrome WebDriver
driver = webdriver.Chrome()

# Abre la URL especificada en el navegador
driver.get(" SERVER URL ")

# Pausa la ejecución durante 2 segundos para que la página cargue por completo
time.sleep(2)

# Busca el botón usando su XPath y haz clic en él
driver.find_element(...)...

# Pausa la ejecución durante 2 segundos para que puedas ver el resultado del clic
time.sleep(2)

# Cierra el navegador y finaliza la sesión de WebDriver
driver.quit()