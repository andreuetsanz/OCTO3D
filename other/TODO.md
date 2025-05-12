# TODO
- Probar a conectar los datos que obtengo de nodered a logstas i luego a kafka o ver como funciona al menos probar a conectar lo que sea
- Probar a como lo que se publica recibirlo i guardarlo a mongo o crear la base de kibana
- Mirar de hacer un docker file para por ejemplo en nodered instalar los nodos necesarios automaticamente
- Mirar el error de Verificar tiempo en el flujo de nodered (enviarle correo a jose o algo)

## Andreu

# Done
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