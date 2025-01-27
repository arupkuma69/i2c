import smbus
import time

# I2C address of the Ublox M10 device
UBLOX_M10_I2C_ADDRESS = 0x42  # Replace with the actual address if different

# Initialize the I2C bus
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def read_ublox_m10_data():
    try:
        # Read data from the Ublox M10 device
        # Replace 0x00 with the actual register address you want to read from
        data = bus.read_i2c_block_data(UBLOX_M10_I2C_ADDRESS, 0x00, 32)
        
        # Convert the data to a readable format
        data_str = ''.join(chr(byte) for byte in data)
        
        print("Data from Ublox M10:", data_str)
    except Exception as e:
        print("Error reading data from Ublox M10:", e)

if __name__ == "__main__":
    while True:
        read_ublox_m10_data()
        time.sleep(1)  # Read data every second
