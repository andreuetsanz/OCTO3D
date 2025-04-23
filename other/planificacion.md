# PLANIFICACION DE PROYECTO DE BIG DATA
Autores: Gerard Grau y Andreu Sanz

## 📑 ÍNDICE

### 1. 📘 Introducción  
Breve explicación del propósito y alcance del proyecto.

### 2. 🧱 Estructura del Proyecto  
Descripción general de la organización de carpetas, módulos y componentes principales.

### 3. 🛠️ Tecnologías  
Listado de tecnologías empleadas, su función y cómo se integran en el sistema.

### 4. 📓 Cuaderno  
Explicación del uso de notebooks (Jupyter, etc.) o bitácora del desarrollo.

## 1. 📘 INTRODUCCIÓN
Introduccion del tema

## 2. 🧱 ESTRUCTURA DEL PROYECTO
Separar el proyecto por partes (carpetas o lo que sea)
```
IMPRESSCONTROL
|---📂 Extraccion de datos
|   |--documento
|
|---📂 Gestion de los datos
|
|---📂 Visualizacion de los datos
|
│-- 📂 backup
│-- 📂 other
│-- 📂 res
|
|--readme.md
|--requirments.txt
|--docker_compose.yaml
```
## 3. 🛠️ TECNOLOGÍAS

A continuación se presenta un listado de las tecnologías utilizadas, junto con una breve descripción y su propósito dentro del sistema:

### 🧠 Node-RED  
**Descripción:** Plataforma de desarrollo basada en flujo para programación visual.  
**Uso:** Permite integrar y conectar hardware, APIs y servicios online de manera sencilla.

### 📊 Power BI  
**Descripción:** Herramienta de análisis empresarial de Microsoft.  
**Uso:** Se utiliza para la visualización interactiva de datos y la creación de dashboards dinámicos.

### 🍃 MongoDB  
**Descripción:** Base de datos NoSQL orientada a documentos.  
**Uso:** Almacena grandes volúmenes de datos de forma flexible y escalable.

### 📈 Kibana  
**Descripción:** Interfaz de visualización para datos almacenados en Elasticsearch.  
**Uso:** Permite crear dashboards y gráficos en tiempo real sobre los datos indexados.

### 🔍 Elasticsearch  
**Descripción:** Motor de búsqueda y análisis basado en Lucene.  
**Uso:** Se emplea para la indexación y búsqueda rápida de grandes volúmenes de datos.

### 📬 Kafka  
**Descripción:** Plataforma de streaming distribuido.  
**Uso:** Se encarga de la transmisión de datos en tiempo real entre sistemas de forma eficiente.

### 🧰 Logstash  
**Descripción:** Herramienta de ingesta y procesamiento de logs.  
**Uso:** Procesa, transforma y envía datos a Elasticsearch para su posterior análisis.

## 4. 📓 CUADERNO

### Semana -1 (31/3 - 6/3)
Gerard: Planificacion y estructura

Andreu: Planificacion y estructura

### Semana 0 (7/4 - 13/4)
Gerard:...

Andreu:...

### Semana 1 (14/4 - 20/4)
Gerard:...

Andreu:...

### Semana 2 (21/4 - 27/4)
Gerard:...

Andreu: Conseguir el dato
He plantejat mal lo de com obtindre el dato, perque jo el que vuic es obtindre el dato cada x segons no suscriurem a un topic directament desde octoprint.
he acosneguit recibir desde mqtt amb el plugin de mqtt pero eixe no es el objectiu 
vaig a vore si puc obtindrelo desde http request.
He conseguit pbtindre els datos per http request soles obtinc alguns en falten prou mes tard o conseguire i ja he definit un flux de el programa en la carpeta other

#### TODO
- Definir totes les dades que es volen obtindre i el format correcte
 
### Semana 3 (28/4 - 4/5)
Gerard:...

Andreu:...

### Semana 4 (5/5 - 12/5)
Gerard:...

Andreu:...
