from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configura ChromeOptions para evitar notificaciones
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Inicia el servicio de ChromeDriver (asegúrate de que la ruta sea correcta)
service = Service("C:\\Users\\enzoe\\Desktop\\CHRONIUM\\chromedriver-win64\\chromedriver.exe")

print("lptm programa de mierda")
# Inicia el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre la página web
driver.get("https://csgocases.com") 

print("a mimir")
# Espera a que la página cargue
time.sleep(30)

# Busca el botón por la clase completa y haz clic
try:
    boton_mas = driver.find_element(By.CSS_SELECTOR, "span.button.button-green.button-plus")
    boton_mas.click()
    print("Botón 'más' clicado con éxito")
except Exception as e:
    print(f"Error al intentar hacer clic en el botón: {e}")
    
print("a mimir")
# Espera unos segundos para observar el resultado
time.sleep(30)

# Cierra el navegador
driver.quit()
