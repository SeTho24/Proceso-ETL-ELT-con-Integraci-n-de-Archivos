# Proceso-ETL-ELT-con-Integraci-n-de-Archivos
Integrar y transformar datos provenientes de tres archivos (PDF, Excel y CSV) en una base de datos relacional, con el propósito de generar información estratégica como promedios, procedencias, demanda por carrera, subsistemas más comunes.
 ## 1. Introducción
Esta práctica tiene como propósito integrar y analizar información educativa mediante procesos ETL, con el fin de unificar datos de aspirantes, carreras y planteles dentro de una base de datos relacional. El objetivo principal es desarrollar un modelo de datos que facilite su visualización y análisis en Power BI, apoyando así la toma de decisiones tanto académicas como administrativas.
### 🚀 Herramientas y Requerimientos Utilizados

| 🧰 Herramienta / Requisito     | 📝 Propósito / Uso principal                                                        |
|-------------------------------|-------------------------------------------------------------------------------------|
| 🗄️ **MySQL 8.0**              | Motor de base de datos relacional para almacenar la información integrada          |
| 🧮 **MySQL Workbench**         | Interfaz gráfica para diseño, consulta y administración de la base de datos        |
| 🐍 **Python 3.x**              | Lenguaje utilizado para realizar el procesamiento y transformación de los datos    |
| 📦 **pandas**                 | Librería de Python para manipular archivos Excel y CSV                             |
| 📄 **pdfplumber**             | Librería de Python para extraer información estructurada desde archivos PDF        |
| 📊 **Power BI**               | Plataforma de visualización para crear informes interactivos a partir de los datos |
| 📁 **Archivos fuente**         | PDF de planteles, Excel de aspirantes, CSV de carreras                             |
| 🔗 **MySQL Connector**         | Conexión entre Power BI y la base de datos MySQL                                   |
| 📂 **Sistema operativo**       | Windows (compatible con Python, Power BI, MySQL Workbench)                         |
| 🧩 **Dependencias**            | `pandas`, `pdfplumber`, `openpyxl`, `mysql-connector-python`                       |
| 🛡️ **Permisos necesarios**    | Acceso a los archivos locales y privilegios para instalación de paquetes Python    |


# instalaremos mysqlworkbench como nuestra base de datos.

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/51eb553e-6ee7-4ac4-b371-d2ac1b3174d6" />

despues de la instalacion realizaremos la creacion de la base de datos y sus debidas tablas

<img width="177" height="119" alt="image" src="https://github.com/user-attachments/assets/08828489-4561-4de4-a054-fa81d0f9af0c" />

## Esquema Relacional de la Base de Datos

<img width="443" height="455" alt="image" src="https://github.com/user-attachments/assets/7cd9fce8-4ea0-46e8-b1b3-a321d6d3d2fb" />

##  Proceso ETL

### .1 Extracción de Datos

#### 📄 Procesamiento de PDF (Planteles)
- **Archivo:** `Catalogo_Escuelas_MediaSuperior.pdf`
- **Script:** `Catalogo/scripts_pdf.py`
- **Tecnología:** `pdfplumber`
- **Desafío:** Extracción compleja de tablas con datos incompletos

- <img width="1338" height="208" alt="image" src="https://github.com/user-attachments/assets/047d4a13-4f01-430b-8dac-5e62d40a0c36" />


#### 📊 Procesamiento de Excel (Aspirantes)
- **Archivo:** `Aspirantes/Aspirantes.xlsx`
- **Script:** `Aspirantes/script_excel.py`
- **Tecnologías:** `pandas`, `openpyxl`

- <img width="534" height="214" alt="image" src="https://github.com/user-attachments/assets/0d68cea6-4667-441f-a4ea-cad09521a172" />


#### 📋 Procesamiento de CSV (Carreras)
- **Archivo:** `Carreras/Carreras.csv`
- **Script:** `Carreras/script_csv.py`
- **Tecnología:** `csv` (módulo estándar de Python)


- <img width="441" height="421" alt="image" src="https://github.com/user-attachments/assets/b5a14972-d1da-4716-ae35-c101644cae0e" />

`cada captura mostrada es el resultado despues del script`
---

##  Validación y Limpieza de Datos

### .1 Validación de CURPs

- **Porcentaje de éxito:** 0.9% (9 de 1000 registros)
- **Criterios de validación:**
  - Longitud exacta de 18 caracteres
  - Formato con expresión regular:  
    `^[A-Z]{4}[0-9]{6}[HMX][A-Z]{5}[0-9A-Z]{2}$`
  - Fecha de nacimiento válida
  - Entidad federativa reconocida
  - Sexo válido (`H`, `M` o `X`)
 
## Integracion con Power BI

una ves listo todos los daros que utilizamos, e integramos a la base de datos mediente los scrips que realizamos la exportacion de las tablas en .cvs para su uso 

![Imagen de WhatsApp 2025-07-13 a las 16 19 46_dec9936d](https://github.com/user-attachments/assets/64fd4452-936b-4663-bf13-e11934d4be17)

![Imagen de WhatsApp 2025-07-13 a las 16 19 56_cd5d5246](https://github.com/user-attachments/assets/4faea1d0-bde3-4910-934b-f5d0a31bfdeb)

![Imagen de WhatsApp 2025-07-13 a las 16 20 31_b9865bbc](https://github.com/user-attachments/assets/c792997f-37d8-4a03-858c-22acfc28b4de)

<img width="458" height="442" alt="image" src="https://github.com/user-attachments/assets/8972e5a3-61ca-4c01-8f05-8b64d7fd9e6b" />

una ves realizado esto lo importamos a Power BI.

<img width="481" height="483" alt="image" src="https://github.com/user-attachments/assets/b185fce0-aed7-4aa1-b026-66ebd26c76e2" />

y seleccionamos las tablas que vamos a utilizar.

![Imagen de WhatsApp 2025-07-13 a las 16 47 59_6f171bb7](https://github.com/user-attachments/assets/c9ec887f-8c16-4c60-8a39-58a4896c1386)

deberiamos tener algo similar a lo siguiente.


![Imagen de WhatsApp 2025-07-13 a las 16 53 09_158eb24c](https://github.com/user-attachments/assets/f0e5c1a0-4802-44cc-8e08-94ed89ddec92)


## 📊 Análisis y Visualizaciones Propuestas

### 1. Mejores promedios por escuela
- **Instrucción:** Agrupar por *Clave de Centro de Trabajo (CCT)* y calcular el promedio general.
- **Resultado esperado:** Tabla o gráfica de barras con las escuelas mejor evaluadas.
- **Aplicación:** Identificar planteles con alto desempeño para establecer convenios o programas de ingreso directo.

- ![Imagen de WhatsApp 2025-07-13 a las 16 59 38_a02e0c08](https://github.com/user-attachments/assets/58e917dc-19a7-4952-9472-73b09f17a139)

### 2. Distribución de estudiantes por estado
- **Instrucción:** Contar estudiantes agrupados por *ENTIDAD*.
- **Resultado esperado:** Gráfica de pastel o barras.
- **Aplicación:** Visualizar de qué estados provienen los aspirantes y orientar campañas de promoción.

- ![Imagen de WhatsApp 2025-07-13 a las 17 00 35_1c945fb6](https://github.com/user-attachments/assets/39b5d011-de54-4da9-a841-97e81f7c0e82)



### 3. Clasificación por sexo por carrera
- **Instrucción:** Agrupar por *Carrera* y contar estudiantes por *Sexo*.
- **Resultado esperado:** Gráfica de barras agrupadas por carrera y género.
- **Aplicación:** Evaluar equidad de género y fomentar inclusión en carreras con baja representación.

- 

### 4. Carrera con más demanda
- **Instrucción:** Contar estudiantes por *Carrera*.
- **Resultado esperado:** Gráfica de barras.
- **Aplicación:** Identificar programas que requieren más recursos o podrían expandirse.

- ![Imagen de WhatsApp 2025-07-13 a las 17 02 17_a1ee0317](https://github.com/user-attachments/assets/1af0af28-40f7-44ee-a514-9b0368cc3e46)


### 5. Rango de edad de los estudiantes
- **Instrucción:** Agrupar por rangos de edad (ej. 17–19, 20–22) si hay edad o fecha de nacimiento.
- **Resultado esperado:** Histograma.
- **Aplicación:** Ajustar estrategias pedagógicas y servicios al perfil etario.

- ![Imagen de WhatsApp 2025-07-13 a las 17 07 45_03908447](https://github.com/user-attachments/assets/ad99b87d-42ad-4289-9bde-a417aea12692)


### 6. Municipios con más estudiantes
- **Instrucción:** Agrupar por *MUNICIPIO* y contar registros.
- **Resultado esperado:** Tabla o mapa.
- **Aplicación:** Determinar ubicaciones clave para ferias vocacionales o servicios.

- ![Imagen de WhatsApp 2025-07-13 a las 17 08 13_22fba765](https://github.com/user-attachments/assets/fd19d846-fc93-457b-8913-902cf918e74d)


### 7. Comparación de promedios por carrera
- **Instrucción:** Agrupar por *Carrera* y calcular el promedio general.
- **Resultado esperado:** Tabla o gráfica de barras.
- **Aplicación:** Evaluar desempeño académico por tipo de carrera.

- ![Imagen de WhatsApp 2025-07-13 a las 17 15 00_3a59dab8](https://github.com/user-attachments/assets/f81cd761-7ba1-4e1b-b73a-0d3f999035a8)


### 8. Promedio general por estado
- **Instrucción:** Agrupar por *ENTIDAD* y calcular el promedio escolar.
- **Resultado esperado:** Tabla o mapa.
- **Aplicación:** Identificar regiones con mejor preparación académica previa.

- ![Imagen de WhatsApp 2025-07-13 a las 17 16 21_a4afcbb2](https://github.com/user-attachments/assets/bef68f2e-be79-4d6b-80b2-a700b832fab6)


### 9. Número de estudiantes por subsistema
- **Instrucción:** Contar estudiantes por *SUBSISTEMA*.
- **Resultado esperado:** Gráfica de barras o pastel.
- **Aplicación:** Conocer el origen institucional (CBTIS, CETIS, CECYTE, etc.) y establecer alianzas.

- ![Imagen de WhatsApp 2025-07-13 a las 17 17 55_0226afab](https://github.com/user-attachments/assets/08607cb6-669f-427b-9b7c-dcd7637ea66f)


### 10. Escuelas de procedencia con más estudiantes
- **Instrucción:** Contar por *CCT (preparatoria)*.
- **Resultado esperado:** Tabla de frecuencia o gráfica.
- **Aplicación:** Detectar escuelas clave para convenios o difusión.

- ![Imagen de WhatsApp 2025-07-13 a las 17 24 01_4308e0fb](https://github.com/user-attachments/assets/c8574ad9-f60a-46e6-a1c4-2de5079de430)


### 11. Relación entre promedio escolar y tipo de subsistema
- **Instrucción:** Agrupar por *SUBSISTEMA* y calcular promedio.
- **Resultado esperado:** Tabla comparativa.
- **Aplicación:** Medir el nivel académico según el subsistema de origen.

- ![Imagen de WhatsApp 2025-07-13 a las 17 25 45_12797e94](https://github.com/user-attachments/assets/8c00a0a5-74f4-4be8-bce8-00ca0c11c8a0)


### 12. Top 10 localidades con más estudiantes
- **Instrucción:** Contar estudiantes por *LOCALIDAD* y ordenar descendente.
- **Resultado esperado:** Tabla o gráfica.
- **Aplicación:** Focalizar esfuerzos en zonas con mayor número de aspirantes.

- ![Imagen de WhatsApp 2025-07-13 a las 17 26 46_7824d297](https://github.com/user-attachments/assets/d9f576dd-97a6-40c4-9eb8-1dc7170b27cf)


### 13. Carreras menos demandadas
- **Instrucción:** Contar estudiantes por *Carrera* y ordenar ascendentemente.
- **Resultado esperado:** Tabla simple.
- **Aplicación:** Revisar relevancia del programa y reforzar difusión si es necesario.

- ![Imagen de WhatsApp 2025-07-13 a las 17 31 36_8bb9ef96](https://github.com/user-attachments/assets/4bc6c7af-461a-4111-aead-5dcc215fd6e5)


### 14. Mapa de calor por estado y municipio
- **Instrucción:** Agrupar por *ENTIDAD* y *MUNICIPIO*, contar estudiantes y graficar en mapa.
- **Resultado esperado:** Mapa geográfico con intensidad por número de estudiantes.
- **Aplicación:** Visualizar distribución territorial del alumnado.

- ![Imagen de WhatsApp 2025-07-13 a las 17 41 44_2d016d4e](https://github.com/user-attachments/assets/07add3d1-ed37-4a48-ac6d-0ca38ae00bde)


### 15. Municipios más productivos vs más numerosos
- **Instrucción:** Comparar municipios con mayor número de estudiantes vs mayor promedio escolar.
- **Resultado esperado:** Tabla comparativa o doble gráfica.
- **Aplicación:** Evaluar si el volumen estudiantil coincide con el rendimiento académico.

- ![Imagen de WhatsApp 2025-07-13 a las 17 43 14_3c3aa170](https://github.com/user-attachments/assets/44f50a30-2fb1-4dbc-8714-9fde3f8587cc)


## 🧾 Conclusión

El presente trabajo logró integrar y transformar datos educativos provenientes de diversas fuentes —PDF, Excel y CSV— mediante un proceso ETL desarrollado en Python. Esta información fue consolidada en una base de datos relacional en MySQL y visualizada de manera interactiva en Power BI.  
Gracias a este enfoque, se facilitaron distintos análisis, como la identificación de escuelas con mejores promedios, la distribución geográfica de los estudiantes, y la demanda por carrera, entre otros.  
Estos resultados aportan una herramienta útil para la toma de decisiones académicas y administrativas, permitiendo identificar áreas de oportunidad, fortalecer programas educativos y dirigir esfuerzos institucionales con mayor precisión.

---

## 👨‍💻 Autores del trabajo

- **Ever Omar Moreno Nieto**  
- **Sebastián de Jesús Santiago Nieva**


