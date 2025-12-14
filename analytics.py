import json

# -----------------------------
# Cargar datos procesados
# -----------------------------
with open("data-lake/processed/ventas_processed.json", "r", encoding="utf-8") as f:
    ventas = json.load(f)

with open("data-lake/processed/clientes_processed.json", "r", encoding="utf-8") as f:
    clientes = json.load(f)

with open("data-lake/processed/productos_processed.json", "r", encoding="utf-8") as f:
    productos = json.load(f)

# -----------------------------
# 1️⃣ Ventas por producto
# -----------------------------
ventas_por_producto = {}

for venta in ventas:
    for producto in venta["productos"]:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio_unitario"]
        total = cantidad * precio

        if nombre not in ventas_por_producto:
            ventas_por_producto[nombre] = {"unidades_vendidas": 0, "total_vendido": 0}

        ventas_por_producto[nombre]["unidades_vendidas"] += cantidad
        ventas_por_producto[nombre]["total_vendido"] += total

resultado_ventas = [{"nombre_producto": k, **v} for k, v in ventas_por_producto.items()]

with open("data-lake/analytics/ventas_por_producto.json", "w", encoding="utf-8") as f:
    json.dump(resultado_ventas, f, indent=4)

# -----------------------------
# 2️⃣ Clientes frecuentes
# -----------------------------
clientes_frecuentes = {}

for cliente in clientes:
    nombre_cliente = cliente["nombre"]
    clientes_frecuentes[nombre_cliente] = {"compras_realizadas": 0, "total_compras": 0}

for venta in ventas:
    nombre_cliente = venta["cliente"]
    total_venta = venta["total"]
    if nombre_cliente in clientes_frecuentes:
        clientes_frecuentes[nombre_cliente]["compras_realizadas"] += 1
        clientes_frecuentes[nombre_cliente]["total_compras"] += total_venta

resultado_clientes = [{"nombre_cliente": k, **v} for k, v in clientes_frecuentes.items()]

with open("data-lake/analytics/clientes_frecuentes.json", "w", encoding="utf-8") as f:
    json.dump(resultado_clientes, f, indent=4)

# -----------------------------
# 3️⃣ Ingresos totales
# -----------------------------
total_ingresos = sum(venta["total"] for venta in ventas)

with open("data-lake/analytics/ingresos_totales.json", "w", encoding="utf-8") as f:
    json.dump({"total_ingresos": total_ingresos}, f, indent=4)

print(" Analytics generados correctamente en data-lake/analytics")

# -----------------------------
# 4️⃣ Ventas por método de pago
# (MANTENIMIENTO PERFECTIVO)
# -----------------------------

ventas_por_metodo_pago = {}

for venta in ventas:
    metodo = venta["metodo_pago"]
    total = venta["total"]

    if metodo not in ventas_por_metodo_pago:
        ventas_por_metodo_pago[metodo] = 0

    ventas_por_metodo_pago[metodo] += total

resultado_metodo_pago = [
    {"metodo_pago": k, "total_vendido": v}
    for k, v in ventas_por_metodo_pago.items()
]

with open("data-lake/analytics/ventas_por_metodo_pago.json", "w", encoding="utf-8") as f:
    json.dump(resultado_metodo_pago, f, indent=4)

print(" Ventas por método de pago generadas correctamente")
