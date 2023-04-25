import asyncio
import streamlit as st
from modbus_tcp_master import scan_registers_async


async def async_main(ip_address, port, register_type, start_address, end_address):
    log_messages = []
    await scan_registers_async(ip_address, port, register_type, start_address, end_address,
                               callback=log_messages.append)
    return log_messages


st.set_page_config(page_title="Modbus TCP Scanner", layout="centered")
st.title("Modbus TCP Scanner")

ip_address = st.text_input("IP Address", value="10.56.132.128")
port = st.number_input("Port", value=502, step=1)
register_type = st.selectbox("Register Type", ["Holding Register", "Input Register", "Coil", "Discrete Input"])
start_address = st.number_input("Start Address", value=0, step=1)
end_address = st.number_input("End Address", value=65535, step=1)

if st.button("Scan Registers"):
    with st.spinner("Scanning..."):
        log_messages = asyncio.run(async_main(ip_address, port, register_type, start_address, end_address))

    with st.expander("Log Output"):
        for log_message in log_messages:
            st.write(log_message)
