# -----------------------------------------------------------------------------
# --- Descripcion           : Script para hacer Web Scraping en DDTech.mx
# --- Autor                 : Giovani Minutti Mazzocco
# --- Versión               : 1.0.0 
# --- Funcionalidades       : 
#   - Extrae título, precio, SKU, descripción, disponibilidad y URL de productos.
#   - Guarda los datos en un archivo CSV.
#   - Maneja errores y espera entre requests.

# --- Requisitos            : Python 3.x, Selenium, BeautifulSoup, WebDriver Manager para Python
 
#   Versión | Fecha      | Autor                     | Descripción de Cambios
#   --------|------------|---------------------------|--------------------------------------
#   1.0.0   | 30/08/2025 | Giovani Minutti Mazzocco  | Versión inicial del script     
# ------------------------------------------------------------------------------------------

# Importamos las librerias a usar.

# --------------------------------------------------------
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html5lib
from icecream import ic
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

# --------------------------------------------------------
# Otras librerias basicas de Python
import os
import sys
import csv
import time
import warnings
from datetime import datetime
from os import system
import re
from urllib.parse import urljoin

sys.stdout.reconfigure(encoding='utf-8')

system("cls")

# --------------------------------------------------------
# Esta variable la utiliza WebDriver Manager
os.environ['WDM_LOG_LEVEL'] = '0'

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "0"
os.environ["GRPC_VERBOSITY"] = "NONE"

warnings.filterwarnings("ignore")


from typing import Optional

driver: Optional[webdriver.Chrome] = None

def init_driver():
    global driver
    if driver is None:
        # Configuramos las opciones para que no se vea el navegador
        service = Service(executable_path="chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_argument('--headless=new')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_argument('--silent')
        option.add_argument('--log-level=3')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-logging')
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

        driver = webdriver.Chrome(service=service, options=option) 

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Funcion para cerrar el driver al finalizar
def close_driver():
    global driver
    if driver:
        driver.quit()
        driver = None

def scrape_with_selenium(url, save_html=False):
    global driver
    
    try:
        # Inicializar driver si no existe
        if driver is None:
            init_driver()
        if driver is None:
            print("❌ Error: No se pudo inicializar el driver de Selenium.")
            return None
            
        driver.get(url)
            
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
            
        # Esperar algunos segundos para que el contenido dinamico sea generado
        time.sleep(3)
            
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        if save_html:
            with open("pagina_guardada.txt", "w", encoding="utf-8") as f:
                f.write(soup.prettify())
            print()
            print(f"📁 El Archivo 'pagina_guardada.txt' fue creado con Exito.")

        product_data = {}
        
        title_selector = 'title'       
        title_element = soup.select_one(title_selector)
        if title_element:
            product_data['titulo'] = title_element.get_text(strip=True)
        else:
            product_data['titulo'] = 'No encontrado'

        price_selector = 'span[class*="price"]'       
        price_element = soup.select_one(price_selector)
        if price_element:
            price_text = price_element.get_text(strip=True)
            price_clean = re.sub(r'[^\d.,]', '', price_text)
            product_data['precio'] = price_clean if price_clean else price_text
        else:
            product_data['precio'] = 'No encontrado'

        sku_match = re.search(r'id=(\d+)', url)
        product_data['sku'] = sku_match.group(1) if sku_match else 'No encontrado'
        
        # Obtenemos - Descripcion
        description_selector = '[class*="description-container"]'
        desc_element = soup.select_one(description_selector)
        if desc_element:
            product_data['descripcion'] = desc_element.get_text(strip=True)[:500]
        else:
            product_data['descripcion'] = 'No encontrado'
        
        availability_selector = '[class="col-sm-9"]'
        avail_element = soup.select_one(availability_selector)
        if avail_element:
            product_data['disponibilidad'] = avail_element.get_text(strip=True)
        else:
            product_data['disponibilidad'] = 'No encontrado'
       
        product_data['url'] = url

        product_data['fecha_scraping'] = time.strftime('%Y-%m-%d %H:%M:%S')
        

        return product_data

    
    except Exception as e:
        print(f"❌  Error con Selenium en {url}: {e}")
        return None

# Funcion para guardar los datos en un archivo CSV
def save_to_csv(data_list, filename='productos_ddtech.csv'):
    if not data_list:
        print("No hay datos para guardar")
        return
    
    fieldnames = [
        'titulo', 'precio', 'sku', 'descripcion', 
        'disponibilidad', 'url', 'fecha_scraping'
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            if isinstance(data_list, list):
                for data in data_list:
                    if data: 
                        writer.writerow(data)
            else:
                writer.writerow(data_list)
        
        print(f"✅ Datos guardados exitosamente en {filename}")
        
    except Exception as e:
        print(f"❌ Error al guardar el CSV: {e}")

def get_product_urls(category_url, max_products=20):
    """
    Extrae los URLs de productos desde una categoría de DDTech.mx
    """
    print(f"🔗 Buscando productos en: {category_url}")
    init_driver()
    global driver
    driver.get(category_url)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(3)
    page_html = driver.page_source
    # Guardar el HTML para análisis
    with open('categoria_ddtech.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    soup = BeautifulSoup(page_html, 'html.parser')
    product_links = []
    # Buscar enlaces dentro de tarjetas de producto
    # Intenta con diferentes selectores comunes
    # Selector ajustado según el HTML real de DDTech
    links = soup.select('div.product-image a[href^="https://ddtech.mx/producto/"]')
    for a in links:
        href = a.get('href')
        if href and href.startswith('https://ddtech.mx/producto/') and 'id=' in href:
            if href not in product_links:
                product_links.append(href)
        if len(product_links) >= max_products:
            break
    print(f"🔎 Se encontraron {len(product_links)} productos.")
    return product_links

def main():
    
    # Lista de URLs para hacer scraping
    categoria = "https://ddtech.mx/productos/computadoras/portatiles"
    urls = get_product_urls(categoria, max_products=10)

    print()    
    print(f"➡️ Iniciando scraping de DDTech...")
    print(f"📊 Total de URLs a procesar: {len(urls)}")
    print()

    all_data = []
    successful_scrapes = 0
    failed_scrapes = 0

    for i, url in enumerate(urls, 1):
        print(f"🔍 Procesando URL {i}/{len(urls)}")
        print(f"🔗 {url}")

        data = scrape_with_selenium(url, save_html=(i == 0))
        
        if data:
            all_data.append(data)
            successful_scrapes += 1
            print()
            print(f"✅ Producto {i} extraído exitosamente")
            print(f"📝 Título        : {data['titulo'][:80]}{'...' if len(data['titulo']) > 80 else ''}")
            print(f"💰 Precio        : $ {data['precio']}")
            print(f"🆔 SKU           : {data['sku']}")
            print(f"📦 Disponibilidad: {data['disponibilidad']}{' (No hay en Existencia)' if data['disponibilidad'] == '0' else ''}")
            print()
        else:
            failed_scrapes += 1
            print(f"❌ Error al extraer producto {i}")
            print()
        
        # Pausa entre requests para no sobrecargar el servidor
        if i < len(urls): 
            print("⏳ Esperando 2 segundos antes de la siguiente URL...")
            time.sleep(2)
            print()

    close_driver()
    
    if all_data:
        save_to_csv(all_data)
        print(f"🎉 Scraping completado!")
        print(f"✅ Productos extraídos exitosamente: {successful_scrapes}")
        print(f"❌ Productos con errores: {failed_scrapes}")
        print(f"📁 Total de productos guardados: {len(all_data)}")
        print()
    else:
        print("❌ No se pudieron extraer datos de ninguna URL")

if __name__ == "__main__":
    main()