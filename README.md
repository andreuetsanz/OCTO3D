# 🧠 OCTO3D - Guía de Instalación

Bienvenido a **OCTO3D**, una solución todo-en-uno para monitoreo y visualización de impresoras 3D, basada en **OctoPrint**, **Node-RED**, **Kibana** y **Power BI**.

---

## ▶️ Cómo iniciar el proyecto

### 🚀 Levantar los servicios

1. Ve a la carpeta [`docker_containers`](docker_containers)
2. Ejecuta:

```bash
docker-compose up -d
```

---

## 👤 Configuración inicial de OctoPrint

1. Accede a: [http://localhost:5000](http://localhost:5000)
2. Crea una cuenta de usuario
3. En configuración, habilita la **impresora virtual**
4. Instala desde el **Plugin Manager** los siguientes plugins:

   * `DisplayLayerProgress`
   * `MQTT`
5. Reinicia OctoPrint
6. Configura el plugin MQTT: en el campo **Host**, escribe `mqtt`

> 📝 *Nota: Ya tienes archivos G-code listos para imprimir. Úsalos para probar el sistema sin necesidad de subir los tuyos.*

---

## 🔑 Obtener API Key de OctoPrint

1. Ve a `Settings > Application Keys`
2. Genera una nueva API key
3. Cópiala
4. Pégala en [`docker_containers/node-red/octoprintapi`](docker_containers/node-red/octoprintapi)

---

## 🔁 Importar flujo en Node-RED

1. Abre: [http://localhost:1880](http://localhost:1880)
2. Menú ≡ > **Import**
3. Pega el contenido del flujo JSON ubicado en [`necessary-files/node-red-flow.json`](necessary-files/node-red-flow.json)
4. Haz clic en **Import** y luego en **Deploy**

---

## 📊 Cargar dashboard en Kibana

1. Abre: [http://localhost:5601](http://localhost:5601)
2. Ve a `Stack Management > Saved Objects`
3. Haz clic en **Import** y selecciona [`necessary-files/Dashboard-kibana.ndjson`](necessary-files/Dashboard-kibana.ndjson)
4. Visualiza los dashboards en la sección **Dashboard**

> 📝 *Ya puedes imprimir. Elige un archivo G-code y empieza a simular.*

---

## 📈 Visualización en Power BI

1. Abre **Power BI Desktop**
2. Ve a **Archivo > Abrir**
3. Carga el archivo [`power_bi/OCTODATA_DASHBOARD.pbix`](power_bi/OCTODATA_DASHBOARD.pbix) proporcionado
4. Configura las credenciales de conexión si es necesario

---

✅ ¡Listo! Tienes **OCTO3D** completamente operativo para simular, monitorear y analizar tus impresiones 3D en tiempo real con dashboards interactivos y potentes herramientas visuales.