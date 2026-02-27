import serial
import time
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

hist_size = 1000
data = np.zeros(hist_size)
X = np.arange(hist_size)

graph = plt.plot(X, data)[0]

while True:
    start = time.time()
    for i in range(hist_size):
        # Read single byte
        byte = ser.read(1)

        data[i] = byte[0]

        # if byte:
        #     print(f"Got byte: {byte[0]:02X}")
        # else:
        #     print("nothing to read")
    end = time.time()
    graph.set_ydata(data)
    plt.draw()
    print(f"took {1 / (end - start) / 1000 * hist_size} khz")
