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

# 📄 Ruta al archivo HTML exportado desde Instagram
html_filename = "pending_follow_requests.html"
html_path = os.path.join(os.path.dirname(__file__), html_filename)

if not os.path.exists(html_path):
    print(f"❌ No se encontró el archivo '{html_filename}' en la carpeta del script.")
    exit()

# 🧼 Parsear el HTML con BeautifulSoup
with open(html_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 🔗 Extraer enlaces de perfil
links = [a["href"] for a in soup.find_all("a", href=True) if "instagram.com" in a["href"]]
print(f"🔍 Se encontraron {len(links)} solicitudes pendientes.")

# 🛠️ Configurar Selenium con Edge
edge_driver_path = r"C:\Users\Klark\Downloads\edgedriver_win64\msedgedriver.exe"  # ← Asegúrate que esta ruta es correcta
options = Options()
options.use_chromium = True
options.add_argument("--log-level=3")
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

# 🔐 Abrir Instagram y esperar login manual
driver.get("https://www.instagram.com/")
input("🔐 Inicia sesión manualmente y presiona Enter para continuar...")

# 🚫 Cancelar solicitudes
canceladas = 0
for link in links:
    try:
        driver.get(link)
        time.sleep(random.uniform(2.5, 4.5))  # Pausa aleatoria

        # Buscar botón "Pendiente" o similar
        buttons = driver.find_elements(By.XPATH, "//button | //div[@role='button']")
        for btn in buttons:
            text = btn.text.strip().lower()
            if any(kw in text for kw in ["pendiente", "solicitud enviada", "cancel request"]):
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
                btn.click()
                time.sleep(1.5)  # Esperar que se abra el menú

                # Buscar opción "Dejar de seguir"
                try:
                    unfollow_btn = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Dejar de seguir')] | //div[@role='button'][contains(text(), 'Dejar de seguir')]"))
                    )
                    unfollow_btn.click()
                    canceladas += 1
                    print(f"✅ Solicitud cancelada: {link}")
                    time.sleep(random.uniform(2, 3))
                    break
                except:
                    print(f"⚠️ No se encontró opción 'Dejar de seguir' en: {link}")
                    break
        else:
            print(f"⚠️ No se encontró botón 'Pendiente' en: {link}")

    except Exception as e:
        print(f"❌ Error en {link}: {e}")
        continue

# ✅ Finalizar
print(f"\n🎉 Proceso completado. Total solicitudes canceladas: {canceladas}")
driver.quit()
