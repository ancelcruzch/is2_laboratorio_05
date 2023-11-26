from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Especifica la ruta completa al ejecutable de ChromeDriver
chrome_driver_path = "/opt/homebrew/bin/chromedriver"

# Configurar el controlador de Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Abrir la calculadora de porcentaje
    driver.get("https://www.calculator.net/percent-calculator.html")

    # Esperar a que la página se cargue completamente
    driver.implicitly_wait(5)

    # Realizar cálculos de porcentaje
    input_value = driver.find_element("id", "cpar1")
    input_value.send_keys("10")

    input_percentage = driver.find_element("id", "cpar2")
    input_percentage.send_keys("50")

    # Ahora buscar el botón de cálculo
    calculate_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Calculate']")
    calculate_button.click()

    # Esperar a que el resultado se cargue completamente
    driver.implicitly_wait(5)

    # Obtener el texto del resultado basado en su xpath
    result_xpath = ".//*[@id = 'content']/p[2]/font/b"
    result = driver.find_element(By.XPATH, result_xpath).text

    print("Prueba exitosa!")

finally:
    # Esperar antes de cerrar el navegador
    time.sleep(2)
    # Cerrar el navegador
    driver.quit()
