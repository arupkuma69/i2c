import smbus
import time

# I2C address of the Ublox M10 device
UBLOX_M10_I2C_ADDRESS = 0x42  # Replace with the actual address if different

# Initialize the I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def read_register(register):
    try:
        # Read a single byte from the specified register
        data = bus.read_byte_data(UBLOX_M10_I2C_ADDRESS, register)
        
        print(f"Data from register 0x{register:02X}: {data:02X}")
    except Exception as e:
        print(f"Error reading data from register 0x{register:02X}: {e}")

if __name__ == "__main__":
    while True:
        # Read data from different registers
        read_register(0x00)  # Replace 0x00 with the actual register address
        read_register(0x01)  # Replace 0x01 with another register address
        read_register(0x02)  # Replace 0x02 with another register address

        time.sleep(1)  # Read data every second
