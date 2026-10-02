# Validación de columnas estructurales

Este trabajo se realizó utilizando el modelo **Snowdon Towers Sample Structural**, Dynamo y Python.

## Objetivo

Leer y clasificar las columnas estructurales del modelo según la nomenclatura de su tipo, generando un reporte que pueda revisarse en Dynamo y exportarse a Excel.

## Entrada

La rutina toma todos los elementos de la categoría **Pilares estructurales** del modelo Revit.

## Funcionamiento

Python obtiene de cada elemento:

- Id
- Tipo
- Nivel

Luego clasifica los tipos de la siguiente manera:

- `CC` → Hormigon
- `W` → Acero W
- `HSS` → Acero HSS
- `SC_` → Pilar de referencia
- Otros → Otro tipo

## Resultado

El resultado se muestra en Dynamo mediante el nodo **Watch** y se exporta a un archivo Excel con las columnas:

**Id | Tipo | Nivel | Clasificacion**

## Limitación

La clasificación depende de los prefijos definidos en el script. Si aparecen nuevos tipos con una nomenclatura diferente, se deberá ampliar la regla.

## Archivos

- `Validacion Columnas Estructurales.dyn`
- `Validacion Columnas.py`
- `Resultado Validacion Pilares.xlsx`
