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

# COMENTARIOS:
# Estrategia de generación de casos de uso centrada en las funcionalidades..

'''
(venv) acruzch@Alains-MacBook-Air IS2_Laboratorio_05 % python test_calculator.py                                               
/Users/acruzch/PycharmProjects/IS2_Laboratorio_05/venv/lib/python3.9/site-packages/urllib3/__init__.py:34: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Prueba exitosa!

'''