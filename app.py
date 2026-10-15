import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("El dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "157.230.214.127"
port = 1883

# Título y tema de la App
st.title("🐱 Dispensador Automático de Comida")
st.write("Control remoto IoT para consentir a tu mascota 🐾")

# Botón 1: Servir Porción
if st.button('🐾 ¡Servir Porción!'):
    act1 = "ON"
    client1 = paho.Client("yos_streamlit")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
    st.success("¡Porción servida! 😺")
else:
    st.write('')

# Botón 2: Cerrar Comedero
if st.button('🛑 Cerrar Comedero'):
    act1 = "OFF"
    client1 = paho.Client("yos_streamlit")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
    st.info("Comedero cerrado 🔒")
else:
    st.write('')

st.write("---")

# Slider para la compuerta del dispensador
values = st.slider('Selecciona la apertura de la compuerta (°)', 0.0, 180.0, 90.0)
st.write('Ángulo de la compuerta:', values)

if st.button('⚙️ Ajustar Compuerta'):
    client1 = paho.Client("yos_streamlit")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a", message)
    st.success(f"Compuerta ajustada a {values}° ✨")
else:
    st.write('')
