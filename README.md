# Mercado Gualanday – Base de Datos NoSQL

Este proyecto implementa una base de datos NoSQL desde cero para el
Mercado Gualanday, utilizando MongoDB, un Data Lake y tecnologías Big Data.

El sistema permite gestionar productos, clientes, ventas y preparar
información para análisis masivo y toma de decisiones.

# Mercado Gualanday – Proyecto Final NoSQL

## Descripción del Proyecto

Este proyecto tiene como objetivo la gestión de un mercado simulado llamado **Mercado Gualanday**, usando **MongoDB** como base de datos NoSQL. Se incluyen las colecciones de clientes, productos y ventas, con datos reales de ejemplo, y se generan informes analíticos sobre ventas, ingresos y clientes frecuentes.

El proyecto permite manejar grandes volúmenes de datos de manera flexible y escalable, demostrando cómo NoSQL puede ser útil en entornos comerciales.

---

## Estructura del Proyecto

- `database/schemas/` → Contiene los esquemas de las colecciones: clientes, productos y ventas.  
- `data-lake/processed/` → Datos limpios listos para análisis.  
- `data-lake/analytics/` → Resultados de los análisis generados por el script `analytics.py`.  
- `analytics.py` → Script en Python que procesa los datos y genera los informes.  
- `src/` → Carpeta opcional para código adicional.  
- `README.md` → Este documento explicativo.  

---

## Contenido de las Colecciones

- **Clientes:** nombre, correo electrónico, teléfono y dirección.  
- **Productos:** nombre, categoría, precio unitario y stock.  
- **Ventas:** fecha, cliente, productos comprados, total y método de pago.  

---

## Cómo Ejecutar el Proyecto

1. Asegúrate de tener Python instalado.  
2. Abre la carpeta raíz del proyecto en tu terminal o Git Bash.  
3. Ejecuta el script principal:

```bash
python analytics.py
