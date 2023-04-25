import asyncio
from pymodbus.client import AsyncModbusTcpClient

async def scan_registers_async(ip_address, port=502, register_type='Holding Register', start_address=0, end_address=65535, callback=None):
    client = AsyncModbusTcpClient(ip_address, port)
    await client.connect()

    if not client.connected:
        callback(f"Cannot connect to Modbus device at {ip_address}:{port}")
        return

    for address in range(start_address, end_address + 1):
        try:
            if register_type == 'Holding Register':
                response = await client.read_holding_registers(address, 1)
            elif register_type == 'Input Register':
                response = await client.read_input_registers(address, 1)
            elif register_type == 'Coil':
               response = await client.read_coils(address, 1)
            elif register_type == 'Discrete Input':
                response = await client.read_discrete_inputs(address, 1)
            else:
                callback(f"Invalid register type: {register_type}")

            if response.isError():
                continue
            else:
                value = response.registers[0] if register_type in ['Holding Register', 'Input Register'] else response.bits[0]
                callback(f'{register_type} {address}: Value:{value}')

        except Exception as e:
            callback(f"Error scanning address {address}: {e}")

    await client.close()
    return
