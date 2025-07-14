import pandas as pd
import os

# Rutas
ruta_csv = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\Carreras.csv"
ruta_salida_sql = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\archivos limpios\carreras.sql"

# Leer el CSV
df = pd.read_csv(ruta_csv)

# Normalizar encabezados
df.columns = [col.strip().lower() for col in df.columns]

# Buscar columna con nombre de carrera
columna_carrera = [col for col in df.columns if "nombre" in col or "carrera" in col][0]

# Generar archivo .sql con INSERTS
with open(ruta_salida_sql, "w", encoding="utf-8") as archivo_sql:
    archivo_sql.write("INSERT INTO carreras (ID_CARRERA, NOMBRE_CARRERA) VALUES\n")

    for idx, nombre in enumerate(df[columna_carrera], start=1):
        carrera = str(nombre).strip().replace("'", "''")
        linea = f"({idx}, '{carrera}')"
        archivo_sql.write(linea + (",\n" if idx < len(df) else ";\n"))

print(f"✅ Archivo SQL generado con {len(df)} registros en formato INSERT.")
