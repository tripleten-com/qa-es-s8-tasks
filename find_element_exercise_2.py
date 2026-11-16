import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa una nueva instancia de Chrome WebDriver
driver = webdriver.Chrome()

# Abre la URL especificada en el navegador
driver.get(" SERVER URL ")

# Pausa la ejecución durante 2 segundos para que la página cargue por completo
time.sleep(2)

# Busca todos los elementos de la página usando un selector XPath
elements = driver...

# Comprueba con len() que el número de elementos encontrados sea mayor que 1
...

# Cierra el navegador y finaliza la sesión de WebDriver
driver...
