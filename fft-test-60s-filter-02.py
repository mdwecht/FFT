#
# Test using FFT to analize log event frequency
#
import numpy as np
import matplotlib.pyplot as plt


# Construct a time signal
Fs = 1                                # Sampling frequency
N = 1024                              # Number of samples
tstep = 1/Fs                          # Sample time interval
t = np.linspace(0, (N-1)*tstep, N)    # Time steps
fstep  = Fs/N                         # Frequency interval
f = np.linspace(0, (N-1)*fstep, N)    # Frequency step


# Initialize array to hold repeating sample pattern
t_pattern = [0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,
             0,0,0,0.0625,0.25,0.375,0.25,0.0625,0,0]
t_array = [0]*(N+len(t_pattern))
repeat_count = int(N/len(t_pattern))
i=0
for j in range(0, repeat_count):
    for k in range(0, len(t_pattern)):
        t_array[i] = t_pattern[k]
        i = i+1
print(t_array)


# Perform FFT
X = np.fft.fft(t_array, n=N)
X_mag = np.abs(X)/N
f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0]/2


# Create Plots
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, t_array[0:int(N)], '.-')
ax2.plot(f_plot, X_mag_plot, '.-')
ax1.set_xlabel('time (s)')
ax2.set_xlabel('frequency (Hz)')
ax1.grid()
ax2.grid()
ax1.set_xlim(0, t[-1])
ax2.set_xlim(0, f_plot[-1])
plt.tight_layout()
plt.savefig('fft-test-60s-filter-02-plot.jpg', bbox_inches='tight')
plt.close('fft-test-60s-filter-02-plot.jpg')
plt.clf


