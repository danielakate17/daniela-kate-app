import streamlit as st

# CONFIGURACIÓN
st.set_page_config(
    page_title="Business Simulator",
    page_icon="💼"
)

# TÍTULO
st.title("💼 Business Simulator")

st.subheader(
    "Simula la utilidad mensual de tu negocio"
)

st.write(
    "Ingresa la información de tus productos y gastos mensuales."
)

# CANTIDAD DE PRODUCTOS
cantidad_productos = st.number_input(
    "📦 ¿Cuántos productos vende tu negocio?",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

productos = []

# PRODUCTOS
st.header("📦 Productos")

for i in range(cantidad_productos):

    st.subheader(f"Producto {i + 1}")

    nombre = st.text_input(
        f"Nombre del producto {i + 1}",
        key=f"nombre{i}"
    )

    precio = st.number_input(
        f"💲 Precio de venta del producto {i + 1} (S/)",
        min_value=0,
        value=0,
        step=1,
        key=f"precio{i}"
    )

    costo = st.number_input(
        f"🏭 Costo por unidad del producto {i + 1} (S/)",
        min_value=0,
        value=0,
        step=1,
        key=f"costo{i}"
    )

    cantidad = st.number_input(
        f"📦 Cantidad vendida del producto {i + 1}",
        min_value=0,
        value=0,
        step=1,
        key=f"cantidad{i}"
    )

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "costo": costo,
        "cantidad": cantidad
    })

# GASTOS
st.header("💸 Gastos Mensuales")

publicidad = st.number_input(
    "📢 Gasto mensual en publicidad (S/)",
    min_value=0,
    value=0,
    step=1
)

alquiler = st.number_input(
    "🏢 Alquiler mensual (S/)",
    min_value=0,
    value=0,
    step=1
)

otros = st.number_input(
    "💡 Otros gastos fijos mensuales (S/)",
    min_value=0,
    value=0,
    step=1
)

# BOTÓN
if st.button("📊 Calcular utilidad mensual"):

    ingresos_totales = 0
    costos_totales = 0
    cantidad_total = 0

    st.header("📈 Resultados por Producto")

    for producto in productos:

        # ICONOS AUTOMÁTICOS
        nombre_lower = producto["nombre"].lower()

        if "blusa" in nombre_lower:
            icono = "👚"

        elif "pantalon" in nombre_lower:
            icono = "👖"

        elif "zapato" in nombre_lower:
            icono = "👟"

        elif "maquillaje" in nombre_lower:
            icono = "💄"

        elif "perfume" in nombre_lower:
            icono = "🧴"

        elif "bolso" in nombre_lower:
            icono = "👜"

        elif "guitarra" in nombre_lower:
            icono = "🎸"

        elif "celular" in nombre_lower:
            icono = "📱"

        elif "laptop" in nombre_lower:
            icono = "💻"

        elif "computadora" in nombre_lower:
            icono = "🖥️"

        elif "audifono" in nombre_lower:
            icono = "🎧"

        elif "reloj" in nombre_lower:
            icono = "⌚"

        elif "camisa" in nombre_lower:
            icono = "👔"

        elif "vestido" in nombre_lower:
            icono = "👗"

        elif "falda" in nombre_lower:
            icono = "🩳"

        elif "gorra" in nombre_lower:
            icono = "🧢"

        elif "joya" in nombre_lower:
            icono = "💍"

        elif "collar" in nombre_lower:
            icono = "📿"

        elif "pizza" in nombre_lower:
            icono = "🍕"

        elif "hamburguesa" in nombre_lower:
            icono = "🍔"

        elif "cafe" in nombre_lower:
            icono = "☕"

        elif "helado" in nombre_lower:
            icono = "🍦"

        elif "pastel" in nombre_lower:
            icono = "🎂"

        elif "galleta" in nombre_lower:
            icono = "🍪"

        elif "pollo" in nombre_lower:
            icono = "🍗"

        elif "libro" in nombre_lower:
            icono = "📚"

        elif "pelota" in nombre_lower:
            icono = "⚽"

        elif "bicicleta" in nombre_lower:
            icono = "🚲"

        elif "carro" in nombre_lower:
            icono = "🚗"

        elif "moto" in nombre_lower:
            icono = "🏍️"

        elif "sofa" in nombre_lower:
            icono = "🛋️"

        elif "mesa" in nombre_lower:
            icono = "🪑"

        elif "lampara" in nombre_lower:
            icono = "💡"

        elif "flor" in nombre_lower:
            icono = "🌸"

        elif "mascota" in nombre_lower:
            icono = "🐶"

        else:
            icono = "📦"

        # CÁLCULOS
        ingreso = (
            producto["precio"]
            * producto["cantidad"]
        )

        costo_total = (
            producto["costo"]
            * producto["cantidad"]
        )

        ganancia = ingreso - costo_total

        ingresos_totales += ingreso
        costos_totales += costo_total
        cantidad_total += producto["cantidad"]

        # RESULTADOS DEL PRODUCTO
        st.subheader(
            f"{icono} {producto['nombre']}"
        )

        st.write(
            f"💰 Ingresos: S/ {ingreso:,}"
        )

        st.write(
            f"🏭 Costos: S/ {costo_total:,}"
        )

        st.write(
            f"✅ Ganancia: S/ {ganancia:,}"
        )

    # GASTOS TOTALES
    gastos_totales = (
        costos_totales
        + publicidad
        + alquiler
        + otros
    )

    utilidad = ingresos_totales - gastos_totales

    # RESULTADOS FINALES
    st.header("📊 Resultados Finales")

    st.success(
        f"💰 Ingresos mensuales totales: S/ {ingresos_totales:,}"
    )

    st.info(
        f"💸 Gastos mensuales totales: S/ {gastos_totales:,}"
    )

    # UTILIDAD
    if utilidad > 0:

        st.success(
            f"✅ Utilidad mensual: S/ {utilidad:,}"
        )

        st.balloons()

        if utilidad >= 1000:

            st.write(
                "🟢 Tu negocio es rentable"
            )

        else:

            st.write(
                "🟡 Tu negocio genera ganancias, pero puede mejorar"
            )

    elif utilidad < 0:

        st.error(
            f"❌ Pérdida mensual: S/ {abs(utilidad):,}"
        )

        st.write(
            "🔴 Necesitas reducir gastos o aumentar ventas"
        )

    else:

        st.warning(
            "⚠️ No hay ganancias ni pérdidas"
        )

    # MARGEN DE GANANCIA
    if ingresos_totales > 0:

        margen = (
            utilidad / ingresos_totales
        ) * 100

        st.write(
            f"📌 Margen de ganancia: {margen:.1f}%"
        )

    # PRECIO PROMEDIO
    if cantidad_total > 0:

        precio_promedio = (
            ingresos_totales / cantidad_total
        )

        st.write(
            f"📌 Precio promedio de venta: S/ {precio_promedio:,.2f}"
        )
