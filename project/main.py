from src.scraper.utils import get_firefox_driver
from src.scraper.ddtech import DDTechParentScraper, DDTechDetailScraper
import time
from selenium.webdriver.common.by import By


def test_ddtech_scraper():
    """Prueba el scraper de DDTech paso a paso"""

    print("🚀 Iniciando prueba del scraper DDTech...")
    print("📍 URL objetivo: https://ddtech.mx/productos/computadoras/portatiles")

    # Crear driver con headless=False para ver lo que pasa
    driver = get_firefox_driver(headless=False)

    try:
        print("\n" + "=" * 50)
        print("📋 PASO 1: Obteniendo enlaces de productos...")
        print("=" * 50)

        parent_scraper = DDTechParentScraper(driver)
        product_links = parent_scraper.scroll_and_collect()  # ✅ corregido

        print(f"\n✅ Enlaces encontrados: {len(product_links)}")

        if not product_links:
            print("❌ No se encontraron enlaces de productos")
            print("\n🔧 DEBUGGING TIPS:")
            print("- Verificar que la página cargue correctamente")
            print("- Inspeccionar selectores con DevTools")
            print("- Revisar si hay captcha o bloqueo")
            return

        # Mostrar algunos enlaces encontrados
        print("\n📝 Primeros 5 enlaces:")
        for i, link in enumerate(product_links[:5], 1):
            print(f"   {i}. {link}")

        # PASO 2: Probar scraper de detalles con un producto
        if product_links:
            print("\n" + "=" * 50)
            print("🔍 PASO 2: Probando extracción de datos...")
            print("=" * 50)

            test_url = product_links[0]
            print(f"🎯 Probando con: {test_url}")

            detail_scraper = DDTechDetailScraper(driver, test_url)
            product_data = detail_scraper.get_all_data()

            print("\n📊 Datos extraídos:")
            print("-" * 30)
            print(f"Marca: {product_data.get('marca', 'No encontrada')}")
            print(f"Nombre: {product_data.get('nombre', 'No encontrado')}")
            print(f"Precio: ${product_data.get('precio', 'No encontrado')}")
            print(f"Descripción: {product_data.get('descripcion', 'No encontrada')}")

            if 'error' in product_data:
                print(f"⚠️ Error encontrado: {product_data['error']}")

        print("\n" + "=" * 50)
        print("✅ Prueba completada")
        print("=" * 50)

    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()

    finally:
        print("\n⏳ Cerrando navegador en 10 segundos...")
        time.sleep(10)
        driver.quit()


def inspect_page_structure():
    """Inspecciona la estructura de la página para identificar selectores"""

    print("🔍 Inspeccionando estructura de la página...")
    driver = get_firefox_driver(headless=False)

    try:
        driver.get("https://ddtech.mx/productos/computadoras/portatiles")
        time.sleep(5)

        print("\n📋 Analizando elementos de la página...")

        # Buscar elementos que podrían contener productos
        potential_selectors = [
            "article",
            ".card",
            ".product",
            ".item",
            "[class*='product']",
            "[class*='item']",
            "[data-product]",
            ".grid > div",
        ]

        for selector in potential_selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    print(f"✅ {selector}: {len(elements)} elementos")
                else:
                    print(f"❌ {selector}: 0 elementos")
            except Exception as e:
                print(f"⚠️  {selector}: Error - {e}")

        # Buscar enlaces
        all_links = driver.find_elements(By.TAG_NAME, "a")
        product_like_links = []

        for link in all_links:
            href = link.get_attribute("href")
            if href and ("laptop" in href.lower() or "producto" in href.lower()):
                product_like_links.append(href)

        print(f"\n🔗 Enlaces que parecen productos: {len(product_like_links)}")
        for i, link in enumerate(product_like_links[:3], 1):
            print(f"   {i}. {link}")

        input("\n⏸️  Presiona Enter cuando hayas terminado de inspeccionar...")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("Selecciona una opción:")
    print("1. Probar scraper completo")
    print("2. Inspeccionar estructura de la página")

    choice = input("Opción (1 o 2): ").strip()

    if choice == "1":
        test_ddtech_scraper()
    elif choice == "2":
        inspect_page_structure()
    else:
        print("Opción no válida")
