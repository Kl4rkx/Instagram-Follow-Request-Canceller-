# Instagram Follow Request Canceller 🚫

Este script automatiza la cancelación de solicitudes de seguimiento pendientes en Instagram usando Selenium y Microsoft Edge.

## 📦 Requisitos

- Python 3.8+
- Microsoft Edge instalado
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) compatible con tu versión de Edge
- Paquetes de Python:
  ```bash
  pip install selenium


## 📁 Archivos necesarios
main.py: Script principal que automatiza la cancelación

pending_follow_requests.html: Archivo exportado desde Instagram con los usuarios pendientes

## 📌 Importante: El archivo pending_follow_requests.html debe estar en la misma carpeta que el script main.py. Esto permite que el script lo detecte automáticamente sin necesidad de modificar rutas.

## ⚙️ Cómo usar
1. Exporta tu archivo desde Instagram:

- Ve a Instagram Data Download

- Descarga tu archivo pending_follow_requests.html

2. Coloca el archivo en la misma carpeta que main.py

3. Descarga el Edge WebDriver que coincida con tu versión de Edge y colócalo en una ruta accesible. Luego, edita esta línea en el script para que apunte al archivo msedgedriver.exe:
  ```Python
edge_driver_path = r"C:\Users\TuUsuario\Downloads\edgedriver_win64\msedgedriver.exe"
  ```
4. Ejecuta el script:
  ```Bash
python main.py
  ```
5. Inicia sesión manualmente en la ventana del navegador cuando se te indique

6. El script recorrerá todos los perfiles y cancelará las solicitudes que estén marcadas como "Pendiente"

## ✅ Resultado
- Verás en la terminal cuántas solicitudes han sido canceladas

- El script ignora errores y continúa con el resto

- Al final, se mostrará el total de cancelaciones realizadas

## ⚠️ Advertencia
Este script interactúa con Instagram de forma automatizada. Usa el script con moderación para evitar bloqueos temporales o restricciones en tu cuenta.

No se recomienda ejecutar más de 50 cancelaciones seguidas sin pausas. Instagram puede detectar actividad automatizada si se abusa del proceso.
