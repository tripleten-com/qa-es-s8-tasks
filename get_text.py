import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pausa la ejecución durante 2 segundos para que la página cargue por completo
time.sleep(2)

# Busca el campo FROM (Desde) y rellénalo
driver...

# Busca el campo TO (Hasta) y rellénalo
driver...

time.sleep(2)

# Obtén el texto del modo "Fastest" (Más rápido)
mode = ...

time.sleep(2)

# Comprueba que el texto de la variable mode sea "Fastest"
assert ...

driver.quit()
