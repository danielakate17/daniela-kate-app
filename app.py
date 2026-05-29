import streamlit as st

# CONFIGURACIÓN
st.set_page_config(page_title="Business Simulator", page_icon="💼")

# TÍTULO
st.title("💼 Business Simulator")
st.subheader("Simula las ganancias de tu negocio")

st.write("Ingresa los datos de tu negocio:")

# INPUTS
precio = st.number_input("💲 Precio del producto", min_value=0.0)

cantidad = st.number_input("📦 Cantidad vendida", min_value=0)

costo_producto = st.number_input("🏭 Costo por producto", min_value=0.0)

publicidad = st.number_input("📢 Gasto en publicidad", min_value=0.0)

alquiler = st.number_input("🏢 Alquiler / gastos fijos", min_value=0.0)

# BOTÓN
if st.button("📊 Calcular resultados"):

    # CÁLCULOS
    ingresos = precio * cantidad
    costo_total_productos = costo_producto * cantidad
    gastos_totales = costo_total_productos + publicidad + alquiler
    ganancia = ingresos - gastos_totales

    # RESULTADOS
    st.header("📈 Resultados")

    st.success(f"💰 Ingresos totales: S/ {ingresos:.2f}")
    st.info(f"💸 Gastos totales: S/ {gastos_totales:.2f}")

    # GANANCIA O PÉRDIDA
    if ganancia > 0:
        st.success(f"✅ Ganancia neta: S/ {ganancia:.2f}")
        st.balloons()

        if ganancia >= 1000:
            st.write("🟢 Tu negocio es MUY rentable")
        else:
            st.write("🟡 Tu negocio es rentable, pero puede mejorar")

    elif ganancia < 0:
        st.error(f"❌ Pérdida: S/ {abs(ganancia):.2f}")
        st.write("🔴 Necesitas reducir gastos o vender más")

    else:
        st.warning("⚠️ No hay ganancias ni pérdidas")

    # MARGEN DE GANANCIA
    if ingresos > 0:
        margen = (ganancia / ingresos) * 100
        st.write(f"📌 Margen de ganancia: {margen:.1f}%")
