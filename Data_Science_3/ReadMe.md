# Data Science 3 - Analisis
Este repositorio contiene ejercicios enfocados en análisis y procesamiento de datos relacionados con habilidades de caballeros y otros atributos. Los ejercicios incluyen visualización, correlación, estandarización, normalización y partición de datos.

## Ejercicios

### Ejercicio 00: Histograma
- **Objetivo**: Crear un gráfico de histograma para visualizar los datos en el archivo "Test_knight.csv".

![alt text](/req/DS3_Historigram1.png)
![alt text](/req/DS3_Historigram2.png)

### Ejercicio 01: Correlación
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

### Ejercicio 02: Puntos
- **Objetivo**: Crear 4 gráficos utilizando los archivos "Train_knight.csv" y "Test_knight.csv".

![alt text](/req/DS3_points1.png)
![alt text](/req/DS3_points2.png)


### Ejercicio 03: Estandarización
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

### Ejercicio 04: Normalización
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

### Ejercicio 05: División de Datos
- **Objetivo**: Dividir aleatoriamente el archivo "Train_knight.csv" en "Training_knight.csv" y "Validation_knight.csv".

```bash
  $>./split.* Train_knight.csv
  $> ls
  ./split.* Train_knight.csv Training_knight.csv Validation_knight.csv
  $>
```

![alt text](/req/DS3_training.png)