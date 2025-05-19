#!/bin/bash

# Ejecutar el script Python
echo "📦 Ejecutando jsontondjson.py..."
python3 jsontondjson.py
if [ $? -ne 0 ]; then
  echo "❌ Error al ejecutar jsontondjson.py"
  exit 1
fi

# Directorio de chunks
CHUNKS_DIR="chunks"

# Verificar que el directorio existe
if [ ! -d "$CHUNKS_DIR" ]; then
  echo "❌ El directorio '$CHUNKS_DIR' no existe. Asegúrate de que jsontondjson.py generó los archivos .ndjson."
  exit 1
fi

# Subir cada archivo chunk_*.ndjson
for f in "$CHUNKS_DIR"/chunk_*.ndjson; do
  echo "🚀 Subiendo $f"
  curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:9200/_bulk" \
    -H 'Content-Type: application/x-ndjson' \
    --data-binary @"$f"

  echo "✔️  Terminado: $f"
done
