import smbus
import time
import struct

# I2C address of the Ublox M10 device
UBLOX_M10_I2C_ADDRESS = 0x42  # Replace with the actual address if different

# Initialize the I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def read_ubx_nav_pvt():
    try:
        # UBX-NAV-PVT message class and ID
        UBX_NAV_PVT_CLASS = 0x01
        UBX_NAV_PVT_ID = 0x07

        # Request UBX-NAV-PVT message
        request = [0xB5, 0x62, UBX_NAV_PVT_CLASS, UBX_NAV_PVT_ID, 0x00, 0x00]
        bus.write_i2c_block_data(UBLOX_M10_I2C_ADDRESS, 0x00, request)

        # Read 92 bytes from the UBX-NAV-PVT message
        data = bus.read_i2c_block_data(UBLOX_M10_I2C_ADDRESS, 0x00, 92)

        # Check if the message is UBX-NAV-PVT
        if data[0] == UBX_NAV_PVT_CLASS and data[1] == UBX_NAV_PVT_ID:
            # Extract the longitude (bytes 30-33, signed 32-bit integer, scaling factor 1e-7)
            lon = struct.unpack_from('<i', bytes(data[30:34]))[0] * 1e-7
            print(f"Longitude: {lon} degrees")
        else:
            print("Not a UBX-NAV-PVT message")
    except Exception as e:
        print(f"Error reading UBX-NAV-PVT message: {e}")

if __name__ == "__main__":
    while True:
        read_ubx_nav_pvt()
        time.sleep(1)  # Read data every second
