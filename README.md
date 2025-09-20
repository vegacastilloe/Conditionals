# Conditionals
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Conditionals)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 802 ---
- 🌟 * Author: Excel (Vijay A. Verma) BI
- 🌟 * This challenge is contributed by Craig Runciman
 
    - Each group has been assigned candidate numbers, you must find all the subsets of candidate numbers, each subset contains one number from each group, such that the conditions are fully satisfied.
 
 🔰 Este script toma un conjunto de grupos con candidatos numéricos y condiciones lógicas entre ellos, genera todas las combinaciones posibles.
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/dMb6uM2n

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Sequence-Validator/blob/main/sequence_validator.py


# 🧩 Logical Combination Validator – pandas + Python

Este script toma un conjunto de grupos con candidatos numéricos y condiciones lógicas entre ellos, genera todas las combinaciones posibles, filtra las que cumplen las condiciones, y compara la solución con una respuesta esperada.

## 📦 Datos

- **Group**: contiene el nombre de los grupos.
- **Conditions**: contiene el modo o instrucciones de las condiciones que se deben cumplir.
- **Candidates**: contiene los números de candidatos que se le han asignado a cada grupo.
- 
---
## 🧠 Lógica del análisis

1. Lee un archivo Excel desde una URL con grupos, condiciones y candidatos.
2. Genera todas las combinaciones posibles entre candidatos.
3. Evalúa cada combinación según condiciones lógicas entre grupos.
4. Devuelve la solución válida.
5. Compara con la respuesta esperada y marca coincidencias.
6. Devuelve un DataFrame con datos ordenados y una columna `'Match'` que indica si la fila coincide.

---
## 📊 Resultado

Una tabla con:

- My Answer: valores seleccionados por grupo.
- Expected Answer: valores esperados desde el archivo.
- Columna 'Match': True si la fila coincide, False si hay diferencias.

---
## ✨Output:
|   |My Answer|Expected Answer|Match|
|-|-|-|-|
|0|8|8|True|
|1|6|6|True|
|2|9|9|True|
|3|12|12|True|

---
## 🛠️ Requisitos

- Python 3.8+
- pandas
- Archivo Excel

---
## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
logical_validator.py
```
