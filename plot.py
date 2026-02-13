import serial
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') # Force an interactive backend
import numpy as np

# Use 115200 - Ensure your Arduino code matches this!
PORT = '/dev/ttyUSB0' 
BAUD = 115200

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    # Flush initial "boot" garbage from the buffer
    ser.reset_input_buffer()
except Exception as e:
    print(f"Error opening port: {e}")
    exit()

data_points = 1000  
pwm_values = []

print(f"Capturing PWM Signal from {PORT}...")

try:
    while len(pwm_values) < data_points:
        # Added errors='ignore' to prevent the UnicodeDecodeError crash
        line_raw = ser.readline()
        try:
            line = line_raw.decode('utf-8', errors='ignore').strip()
            if line:
                pwm_values.append(int(line))
                # Optional: print progress every 100 samples
                if len(pwm_values) % 100 == 0:
                    print(f"Progress: {len(pwm_values)}/{data_points}")
        except ValueError:
            # Skip lines that aren't valid integers
            continue

    if len(pwm_values) >= data_points:
        print("Data captured! Generating plot...")
        plt.figure(figsize=(12, 6))
        plt.step(range(len(pwm_values)), pwm_values, where='post', color='cyan')
        plt.title("Output Signal")
        plt.xlabel("Sample Index")
        plt.ylabel("Voltage Logic Level (0-1023)")
        plt.grid(True, alpha=0.3)
        plt.ylim(-50, 1100) 
        plt.show()

except KeyboardInterrupt:
    print("\nCapture interrupted by user.")
finally:
    ser.close()
    print("Serial Connection Closed.")