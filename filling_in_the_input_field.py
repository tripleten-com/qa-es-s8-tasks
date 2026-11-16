import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pausa la ejecución durante 2 segundos para que la página cargue por completo
time.sleep(2)

# Busca el campo FROM (Desde) y rellénalo
driver...

# Busca el campo TO (Hasta) y rellénalo
driver...

time.sleep(2)

# Busca el botón "Call a taxi" (Pedir un taxi) y haz clic en él
driver...

# Agrega una espera explícita para que cargue el campo
WebDriverWait(...).until(...)

# Escribe un comentario para el conductor
driver...

time.sleep(2)

# Comprueba que tu comentario sea el esperado
assert ...

driver.quit()
