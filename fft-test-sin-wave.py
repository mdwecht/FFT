import numpy as np
import matplotlib.pyplot as plt

# Construct a time signal
Fs = 1
tstep = 1/Fs
f0 = .0166667
N = 1024
t = np.linspace(0, (N-1)*tstep, N)
fstep = Fs/N
f = np.linspace(0, (N-1)*fstep, N)
y = 1*np.sin(2*np.pi*f0*t)

# Perform FFT
X = np.fft.fft(y)
X_mag = np.abs(X)/N
f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0]/2


# Create Plots
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_mag_plot, '.-')
ax1.set_xlabel('time (s)')
ax2.set_xlabel('frequency (Hz)')
ax1.grid()
ax2.grid()
ax1.set_xlim(0, t[-1])
ax2.set_xlim(0, f_plot[-1])
plt.tight_layout()
plt.savefig('fft-test-sin-wave-plot.jpg', bbox_inches='tight')
plt.close('fft-test-sin-wave-plot.jpg')
plt.clf

