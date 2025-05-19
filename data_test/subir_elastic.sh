 #!/bin/bash

# Directorio de chunks
CHUNKS_DIR="chunks"

# Verificar que el directorio existe
if [ ! -d "$CHUNKS_DIR" ]; then
  echo "❌ El directorio '$CHUNKS_DIR' no existe. Asegúrate de haber generado los archivos .ndjson primero."
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
