import pdfplumber
import os
import re

# Rutas
ruta_pdf = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\Catalogo_Escuelas_MediaSuperior.pdf"
ruta_salida_sql = r"C:\Users\sebas\OneDrive\Escritorio\Actividades escuela\8vo semestre\practica power bi bigdata\archivos limpios\escuelas.sql"

# Nombre de la tabla
nombre_tabla = "escuelas"

# Limpieza básica de texto
def limpiar(texto):
    return texto.strip().replace("'", "''")

# Patrón de CCT
patron_cct = re.compile(r'(\w{2}[A-Z]{3}\d{4}[A-Z])$')

# Lista de registros
registros = []

with pdfplumber.open(ruta_pdf) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            lineas = texto.split('\n')
            for linea in lineas:
                cct_match = patron_cct.search(linea)
                if cct_match:
                    cct = cct_match.group(1)
                    resto = linea[:cct_match.start()].strip()
                    partes = resto.split()
                    if len(partes) >= 5:
                        entidad = partes[0]
                        municipio = partes[1]
                        localidad = partes[2]
                        subsistema = partes[-1]
                        nombre_plantel = ' '.join(partes[3:-1])
                        registros.append((
                            limpiar(entidad),
                            limpiar(municipio),
                            limpiar(localidad),
                            limpiar(nombre_plantel),
                            limpiar(subsistema),
                            limpiar(cct)
                        ))

# Escritura del archivo SQL
with open(ruta_salida_sql, "w", encoding="utf-8") as archivo_sql:
    archivo_sql.write(f"CREATE TABLE {nombre_tabla} (\n")
    archivo_sql.write("    id INT PRIMARY KEY,\n")
    archivo_sql.write("    entidad TEXT,\n")
    archivo_sql.write("    municipio TEXT,\n")
    archivo_sql.write("    localidad TEXT,\n")
    archivo_sql.write("    nombre_plantel TEXT,\n")
    archivo_sql.write("    subsistema TEXT,\n")
    archivo_sql.write("    cct VARCHAR(10)\n")
    archivo_sql.write(");\n\n")

    archivo_sql.write(f"INSERT INTO {nombre_tabla} (id, entidad, municipio, localidad, nombre_plantel, subsistema, cct) VALUES\n")

    for idx, fila in enumerate(registros, start=1):
        entidad, municipio, localidad, nombre_plantel, subsistema, cct = fila
        linea = f"({idx}, '{entidad}', '{municipio}', '{localidad}', '{nombre_plantel}', '{subsistema}', '{cct}')"
        if idx < len(registros):
            archivo_sql.write(linea + ",\n")
        else:
            archivo_sql.write(linea + ";\n")  # Última línea con punto y coma

print(f"✅ Archivo .sql generado con éxito con {len(registros)} registros.")
