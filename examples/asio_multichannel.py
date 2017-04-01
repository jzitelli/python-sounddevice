import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

os = sd.OutputStream(device=14, samplerate=44100, channels=4)

T = 10

t = np.linspace(0, T, T * os.samplerate)

ms = np.stack((0.05*np.sin(440*2*np.pi*t, dtype=np.float32)*np.cos(1*2*np.pi*t, dtype=np.float32)**2,
               0.02*np.sin(1000*2*np.pi*t, dtype=np.float32),
               0.02*np.sin(125*2*np.pi*t, dtype=np.float32),
               0.07*np.cos(80*2*np.pi*t, dtype=np.float32)*np.cos(0.1*2*np.pi*t, dtype=np.float32)**2),
              axis=-1)

n = len(t)
ms[:n//4  ,1:] = 0
ms[:n//2  ,2:] = 0
ms[:3*n//4,3] = 0

print(ms.shape)

os.start()
os.write(ms)
