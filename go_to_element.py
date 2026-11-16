import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Busca el campo Email y rellénalo
...

# Busca el campo Password (Contraseña) y rellénalo
...

# Busca el botón Login (Iniciar sesión) y haz clic en él
...

# Agrega una espera explícita para que cargue la página
...

# Busca el footer (pie de página)
element = ...

# Desplázate hasta que el footer sea visible
driver.execute_script(...)

time.sleep(3)

# Comprueba que el footer contenga la cadena 'Around'
assert ...

driver.quit()
