# 🧠 OCTO3D - Guía de Instalación

Repositorio: `# BDA-SBD_ProjecteFinal`

Bienvenido a **OCTO3D**, una solución integral para monitoreo y visualización de impresoras 3D, usando herramientas como **OctoPrint**, **Node-RED**, **Kibana** y **Power BI**.

---

## ▶️ Para reproducir el proyecto

Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos dentro de la carpeta `docker-container`:

### 📁 Estructura requerida en `docker-container`:

- Un fichero llamado: `octoprintapi`
- Una carpeta `images/` con imágenes necesarias

### 🚀 Luego, sigue estos pasos:

1. Accede a la carpeta `docker-container`
2. Ejecuta:

```bash
docker-compose up -d
```

---

## 👤 Configuración inicial en OctoPrint

1. Accede a OctoPrint en: [http://localhost:5000](http://localhost:5000)
2. Regístrate y crea una cuenta de usuario
3. Habilita la **impresora virtual** en la configuración
4. Importa archivos `.gcode` para poder simular impresiones
5. Instala los siguientes plugins desde el **Plugin Manager**:
   - `DisplayLayerProgress`
   - `MQTT`
6. Reinicia OctoPrint después de instalar los plugins

---

## 🔑 API Key de OctoPrint

1. Ve a `Settings > API`
2. Copia la API Key generada
3. Pégala en el archivo de configuración del sistema OCTO3D: octoprintapi


---

## 🔁 Importar flujo JSON en Node-RED

1. Accede a: [http://localhost:1880](http://localhost:1880)
2. Haz clic en el menú ≡ > **Import > Clipboard**
3. Pega el flujo JSON proporcionado
4. Haz clic en **Import** y luego en **Deploy**

---

## 📊 Visualización en Kibana

1. Accede a: [http://localhost:5601](http://localhost:5601)
2. Ve a `Stack Management > Saved Objects`
3. Haz clic en **Import** y selecciona el dashboard `.ndjson` desde la carpeta correspondiente
4. Revisa los dashboards en la sección **Dashboard**

---

## 📈 Importar en Power BI

1. Abre **Power BI Desktop**
2. Selecciona **Archivo > Abrir**
3. Abre el archivo `.pbix` proporcionado
4. Configura las credenciales de origen de datos si es necesario

---

✅ ¡Listo! Ahora tienes **OCTO3D** completamente configurado para simular, monitorizar y analizar tus impresiones 3D en tiempo real con dashboards interactivos y potentes herramientas de análisis.

---
