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

Sigue estos pasos para ejecutar correctamente el script:

### 1. Exporta tus solicitudes pendientes desde Instagram

Para obtener el archivo `pending_follow_requests.html`, realiza lo siguiente:

- Ve al [Centro de cuentas de Instagram](https://accountscenter.instagram.com/?theme=dark&entry_point=app_settings)  
- Accede a [Tu información y permisos](https://accountscenter.instagram.com/info_and_permissions/?theme=dark)  
- Haz clic en **Exportar tu información**
- Pulsa **Crear exportación**
- Selecciona tu cuenta de Instagram
- Elige **Exportar al dispositivo**
- En **Personalizar información**, desmarca todo excepto:
  - En el apartado **Conexiones**, selecciona solo la casilla de **Seguidores y seguidos**
- Guarda la configuración
- En **Intervalo de fechas**, selecciona **Desde el principio**
- Inicia la exportación

📧 En unos minutos recibirás un correo de Meta con el enlace para descargar tu información.

Una vez descargado el archivo ZIP:

- Ve a la carpeta `connections/followers_and_following/`
- Copia el archivo `pending_follow_requests.html` a la misma carpeta donde está tu script `main.py`

---

### 2. Prepara el entorno

- Asegúrate de tener instalado [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) compatible con tu versión de Microsoft Edge
- Coloca el archivo `msedgedriver.exe` en una ruta accesible
- Edita esta línea en el script para que apunte correctamente al WebDriver:
  ```python
  edge_driver_path = r"C:\Users\TuUsuario\Downloads\edgedriver_win64\msedgedriver.exe"

---

### 3. Ejecuta el script

- Abre una terminal en la carpeta en la que se encuentra el script y ejecuta:
```bash
"python main.py"
```
- Se abrirá una ventana de Edge. Inicia sesión manualmente en Instagram

- El script comenzará a recorrer los perfiles y cancelará las solicitudes que estén marcadas como "Pendiente"

## ✅ Resultado
- Verás en la terminal cuántas solicitudes han sido canceladas

- El script ignora errores y continúa con el resto

- Al final, se mostrará el total de cancelaciones realizadas

## ⚠️ Advertencia
Este script interactúa con Instagram de forma automatizada. Usa el script con moderación para evitar bloqueos temporales o restricciones en tu cuenta.

No se recomienda ejecutar más de 50 cancelaciones seguidas sin pausas. Instagram puede detectar actividad automatizada si se abusa del proceso.

---

## 🌐 Compatibilidad de idioma

Este script está diseñado para funcionar con Instagram configurado en **Español (España)**.

Si usas otro idioma, los textos de los botones pueden variar (por ejemplo, "Pending" en inglés), lo que impediría que el script los detecte correctamente.

📌 Si deseas adaptarlo a otro idioma, puedes modificar las líneas del script que buscan los botones por texto, como `"Pendiente"` o `"Dejar de seguir"`.
