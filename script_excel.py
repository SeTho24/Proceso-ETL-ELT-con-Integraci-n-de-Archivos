import pandas as pd
import os

# Rutas
ruta_excel = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\aspirantes_limpio.xlsx"
ruta_salida_sql = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\archivos limpios\aspirantes.sql"

# Leer Excel
df = pd.read_excel(ruta_excel)

# Renombrar columnas a nombres simples
df.rename(columns={
    'CURP': 'curp',
    'CCT': 'cct',
    'Carreras': 'carrera',
    'Promedio': 'promedio'
}, inplace=True)

# Crear archivo SQL
with open(ruta_salida_sql, 'w', encoding='utf-8') as archivo_sql:
    archivo_sql.write("CREATE TABLE aspirantes (\n")
    archivo_sql.write("    id INT PRIMARY KEY,\n")
    archivo_sql.write("    cct VARCHAR(10),\n")
    archivo_sql.write("    curp VARCHAR(18),\n")
    archivo_sql.write("    carrera VARCHAR(3),\n")
    archivo_sql.write("    promedio INT\n")
    archivo_sql.write(");\n\n")

    archivo_sql.write("INSERT INTO aspirantes (id, cct, curp, carrera, promedio) VALUES\n")

    for idx, row in enumerate(df.itertuples(index=False), start=1):
        cct = str(row.cct).strip().replace("'", "''")
        curp = str(row.curp).strip().replace("'", "''")
        carrera = str(row.carrera).strip().replace("'", "''")
        promedio = float(row.promedio) if not pd.isna(row.promedio) else 0.0
        linea = f"({idx}, '{cct}', '{curp}', '{carrera}', {promedio:.2f})"
        archivo_sql.write(linea + (",\n" if idx < len(df) else ";\n"))

print(f"✅ Archivo SQL generado con {len(df)} registros incluyendo promedio.")
