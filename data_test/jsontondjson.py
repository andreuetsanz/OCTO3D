import json
import os

# Configuración
dir_name = os.path.dirname(__file__)
input_file = os.path.join(dir_name, "octo-data.octo-print.json")
chunk_size = 500                # Nº de documentos por archivo
index_name = "octo-print"        
output_prefix = "chunk_"         

# Cargar datos
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Eliminar el campos
for doc in data:
    doc.pop("_id", None)
    doc.pop("@timestamp", None)
    doc.pop("@version", None)
# Crear carpetas si no existen
os.makedirs(os.path.join(dir_name, "chunks"), exist_ok=True)

# Generar los archivos NDJSON en chunks
for i in range(0, len(data), chunk_size):
    chunk_docs = data[i:i + chunk_size]
    filename = os.path.join(dir_name, f"chunks/{output_prefix}{i // chunk_size:03d}.ndjson")

    with open(filename, "w", encoding="utf-8") as out:
        for doc in chunk_docs:
            out.write(json.dumps({ "index": { "_index": index_name } }) + "\n")
            out.write(json.dumps(doc) + "\n")

    print(f"✔️  Generado: {filename} con {len(chunk_docs)} documentos")
