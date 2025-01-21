# Data Science
Este repositorio contiene varios ejercicios prácticos organizados en diferentes etapas del proceso de Data Science, incluyendo la creación y manipulación de bases de datos, el proceso ETL, visualización de datos, y análisis.

## [Data Science 0 - DB set up](https://github.com/mortiz-d/Piscine_Data_Science/tree/main/Data_Science_0)
Este repositorio contiene los ejercicios para la formación en PostgreSQL, diseñados para practicar la creación y manipulación de bases de datos, tablas y datos.
#### Ejercicio 00: Crear Base de Datos PostgreSQL
- **Objetivo**: Crear una base de datos PostgreSQL llamada `piscineds` y configurar el acceso.
#### Ejercicio 01: Visualizar la Base de Datos
- **Objetivo**: Usar un software para visualizar la base de datos de manera fácil.
#### Ejercicio 02: Crear la Primera Tabla
- **Objetivo**: Crear una tabla en PostgreSQL a partir de un archivo CSV.
#### Ejercicio 03: Creación Automática de Tablas desde CSV
- **Objetivo**: Crear tablas automáticamente a partir de los archivos CSV de la carpeta `customer`.
#### Ejercicio 04: Crear la Tabla "Items"
- **Objetivo**: Crear la tabla `items` usando el archivo CSV correspondiente.

## [Data Science 1 - ETL Piscine](https://github.com/mortiz-d/Piscine_Data_Science/tree/main/Data_Science_1)

Este repositorio contiene los ejercicios prácticos sobre el proceso ETL (Extract, Transform, Load) que implica integrar datos de múltiples fuentes en un único almacén de datos.

![Texto alternativo](/req/DS1_ETL.png)
#### Ejercicio 00: Visualizar la Base de Datos
- **Objetivo**: Usar un software para visualizar fácilmente la base de datos.
#### Ejercicio 01: Tabla de Clientes
- **Objetivo**: Unir todas las tablas `data_202*_***` en una única tabla llamada "customers".

![Texto alternativo](/req/DS1_join.png)
#### Ejercicio 02: Eliminar Duplicados
- **Objetivo**: Eliminar filas duplicadas en la tabla "customers".

![Texto alternativo](/req/DS1_remove_dup.png)
#### Ejercicio 03: Fusión de Tablas
- **Objetivo**: Combinar la tabla "customers" con la tabla "items".

![Texto alternativo](/req/DS1_fussion.png)


## [Data Science 2 - Visualizacion](https://github.com/mortiz-d/Piscine_Data_Science/tree/main/Data_Science_2)
Este repositorio contiene los ejercicios de visualización de datos y análisis de agrupamiento (clustering).

### Ejercicios

#### Ejercicio 00: American Data Pie
- **Objetivo**: Visualizar todos los datos.

![Texto alternativo](/req/DS2_pie2.png)


#### Ejercicio 01: Exploración Inicial de Datos
- **Objetivo**: Filtrar y crear gráficos a partir de los datos de compras.

![Texto alternativo](/req/DS2_Chart1.png)
![Texto alternativo](/req/DS2_Chart2.png)
![Texto alternativo](/req/DS2_Chart3.png)

#### Ejercicio 02: Análisis de Precios
- **Objetivo**: Analizar los precios de los artículos comprados.

![Texto alternativo](/req/DS2_moustache1.png)
![Texto alternativo](/req/DS2_moustache2.png)
![Texto alternativo](/req/DS2_moustache3.png)


#### Ejercicio 03: Gráfico de Barras
- **Objetivo**: Crear gráficos de barras sobre los pedidos de clientes.

![Texto alternativo](/req/DS2_bar1.png)
![Texto alternativo](/req/DS2_bar2.png)

#### Ejercicio 04: Método del Codo
- **Objetivo**: Determinar el número óptimo de grupos para segmentar clientes.

![Texto alternativo](/req/DS2_bar1.png)

#### Ejercicio 05: Clustering de Clientes
- **Objetivo**: Segmentar clientes en grupos para campañas de marketing.

![Texto alternativo](/req/DS2_Cluster1.png)
![Texto alternativo](/req/DS2_Cluster3.png)

![Texto alternativo](/req/DS2_Cluster2.png)
![Texto alternativo](/req/DS2_Cluster4.png)




## [Data Science 3 - Analisis](https://github.com/mortiz-d/Piscine_Data_Science/tree/main/Data_Science_3)
Este repositorio contiene ejercicios enfocados en análisis y procesamiento de datos relacionados con habilidades de caballeros y otros atributos. Los ejercicios incluyen visualización, correlación, estandarización, normalización y partición de datos.

### Ejercicios

#### Ejercicio 00: Histograma
- **Objetivo**: Crear un gráfico de histograma para visualizar los datos en el archivo "Test_knight.csv".

![alt text](/req/DS3_Historigram1.png)
![alt text](/req/DS3_Historigram2.png)

#### Ejercicio 01: Correlación
- **Objetivo**: Calcular los factores de correlación entre las columnas y entender cuáles están más correlacionadas con la columna "knight".
```bash
  knight 1.000000
  Empowered 0.793566
  Stims 0.782914
  Prescience 0.776614
  Recovery 0.776454
  Strength 0.742636
  Sprint 0.733825
  Sensitivity 0.730029
  Power 0.708984
  Awareness 0.696360
  Attunement 0.659610
  Dexterity 0.596534
  Delay 0.590998
  Slash 0.567134
  Force 0.556141
  Lightsaber 0.548236
  Evade 0.456903
  Combo 0.421465
  Burst 0.416294
  Hability 0.415185
  Blocking 0.408042
  Agility 0.358560
  Reactivity 0.330499
  Grasping 0.323872
  Repulse 0.292999
  Friendship 0.253730
  Mass 0.077972
  Survival 0.067016
  Midi-chlorien 0.012838
  Push 0.008303
  Deflection 0.006522
```

#### Ejercicio 02: Puntos
- **Objetivo**: Crear 4 gráficos utilizando los archivos "Train_knight.csv" y "Test_knight.csv".

![alt text](/req/DS3_points1.png)
![alt text](/req/DS3_points2.png)


#### Ejercicio 03: Estandarización
- **Objetivo**: Estandarizar los datos y mostrar un gráfico con los datos estandarizados.
```bash
  $>./standardization.*
  Sensitivity Hability Strength ... Empowered Burst Grasping
  17.99 10.38 122.80 ... 0.26 0.46 0.11
  ...
  Sensitivity Hability Strength ... Empowered Burst Grasping
  1.09 -2.07 1.26 ... 2.29 2.75 1.93
  ...
  $>
```
![alt text](/req/DS3_standarization.png)

#### Ejercicio 04: Normalización
- **Objetivo**: Normalizar los datos y mostrar gráficos con los datos normalizados.

```bash
  $>./normalitation.*
  Sensitivity Hability Strength ... Empowered Burst Grasping
  17.99 10.38 122.80 ... 0.26 0.46 0.11
  ...
  Sensitivity Hability Strength ... Empowered Burst Grasping
  0.52 0.02 0.54 ... 0.91 0.59 0.41
  ...
  $>

```
![alt text](/req/DS3_normalitation.png)

#### Ejercicio 05: División de Datos
- **Objetivo**: Dividir aleatoriamente el archivo "Train_knight.csv" en "Training_knight.csv" y "Validation_knight.csv".

```bash
  $>./split.* Train_knight.csv
  $> ls
  ./split.* Train_knight.csv Training_knight.csv Validation_knight.csv
  $>
```

![alt text](/req/DS3_training.png)

