import smbus
import time

# I2C address of the Ublox M10 device
UBLOX_M10_I2C_ADDRESS = 0x42  # Replace with the actual address if different

# Initialize the I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def read_register(register, length):
    try:
        # Read data from the specified register
        data = bus.read_i2c_block_data(UBLOX_M10_I2C_ADDRESS, register, length)
        
        # Convert the data to a readable format
        data_str = ''.join(chr(byte) for byte in data)
        
        print(f"Data from register 0x{register:02X}: {data_str}")
    except Exception as e:
        print(f"Error reading data from register 0x{register:02X}: {e}")

if __name__ == "__main__":
    while True:
        # Read data from different registers
        read_register(0x00, 32)  # Replace 0x00 with the actual register address
        read_register(0x01, 32)  # Replace 0x01 with another register address
        read_register(0x02, 32)  # Replace 0x02 with another register address

        time.sleep(1)  # Read data every second
