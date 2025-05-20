# TODO
- Comprabar si nodered desde windows funciona
- dasboard de node-red
  - nombre de el archivo @donde
  - imaguen
  - color del estado
- borrar todo i volvver a hacer


- Documentacio


## Tareas futuras para la memoria
- Mirar como hacer para que antes de enviar valida con el data shema

## Andreu

# Done
- Comprobar els errors
- Codi chat gpt
- octoprintapi = [tuapikey]
- Comprobar si en elastica va el pull
- Quiero mejorar la estetica de el dashboard con:
  - Top impresoras por usuario: contar cuantos usuarios tienen el mismo modelo de impresora
  - Top marcas de filamento mas usadas: que marcas de filamento son mas usadas (segun el print_id)
  - Top materiales mas usados
  - Top slicers
  - Contar que impresoras tienen mas tendencia a fallar (conteo del print succesful por impresora)
- Obtener un volumen de datos validos
- Crear un dashboard simple para nodered (tener el cuenta lo de las alertas con orion)
- Mostrar los graficos en powerbi i kibana
- Mirar los datos que podemos mostrar (Que griaficas podemos hacer, que datos son importantes de estudiar)
- Mirar el error de Verificar tiempo en el flujo de nodered (enviarle correo a jose o algo)
- Mirar lo de kafka i lgstas (Ns si gerard ja ho ha mirat)
- Añadir el dato de id de impresion
- Añadir el dato de id de usuario
- El timer del inicio no va muy bien
- Coenctar logstas con kibana i con mongodb 
- Conectar nodered a kafka
- Probar a como lo que se publica recibirlo i guardarlo a mongo o crear la base de kibana
- Probar a conectar los datos que obtengo de nodered a logstas i luego a kafka o ver como funciona al menos probar a conectar lo que sea
- Añadir que detecte los eventos de estado, imprimiendo o no imprimiendo para que que empieze a cojer datos
- Añadir el progreso en porcentaje como int i añadirlo al shema
- Añadir las temperaturas target al flujo y al json
- Comprobar que funciona en una impresora real
- Obtener un dataset de imaguenes random de impresiones i crear un flujo que coja una imaguen random de el dataset para publicarlo por mqtt o simplemente enviarlo por el payload de nodered en base64 (Falta descargar el dataset)
- Modificar en el jsonshema en vez de  print cost como gramos usados de material, modificar tambien en nodered
- Eliminar los datos que no puedo obtener
- Obtener el resto de datos

# Canceled
- Como introducir comandos del terminal por httpreques a octoprint (adelantado en el flujo [httprequest-octoprint-command.json](../Flujos/httprequest-octoprint-command.json)) (No ha sido necesario)
- Obtener la temperatura actual de la habitacion con alexa (No se ha podido obtener pero se ha simulado)
- Mirar porque añade campos adicionales logstash (segun jose es por una practica que icimos)

