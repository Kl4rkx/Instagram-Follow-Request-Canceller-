import os
import time
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Ruta al archivo HTML
html_filename = "pending_follow_requests.html"
html_path = os.path.join(os.path.dirname(__file__), html_filename)

if not os.path.exists(html_path):
    print(f"❌ No se encontró el archivo '{html_filename}' en la carpeta del script.")
    exit()

# Leer y parsear el HTML
with open(html_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extraer enlaces de perfil
links = [a["href"] for a in soup.find_all("a", href=True) if "instagram.com" in a["href"]]
print(f"🔍 Se encontraron {len(links)} solicitudes pendientes.")

# Configurar Selenium con Edge
edge_driver_path = r"C:\Ruta\A\Tu\msedgedriver.exe"  # ← Cambia esta ruta
options = Options()
options.use_chromium = True
options.add_argument("--log-level=3")
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

# Abrir Instagram y esperar login manual
driver.get("https://www.instagram.com/")
input("🔐 Inicia sesión manualmente y presiona Enter para continuar...")

# Cancelar solicitudes
canceladas = 0
for link in links:
    try:
        driver.get(link)
        time.sleep(random.uniform(2.5, 4.5))  # Pausa aleatoria

        # Esperar hasta que el botón esté presente
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        buttons = driver.find_elements(By.TAG_NAME, "button")

        for btn in buttons:
            if "Solicitud enviada" in btn.text or "Cancel request" in btn.text:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
                btn.click()
                canceladas += 1
                print(f"✅ Solicitud cancelada: {link}")
                time.sleep(random.uniform(2, 3))
                break
        else:
            print(f"⚠️ No se encontró botón de cancelación en: {link}")

    except Exception as e:
        print(f"❌ Error en {link}: {e}")
        continue

print(f"\n🎉 Proceso completado. Total solicitudes canceladas: {canceladas}")
driver.quit()
