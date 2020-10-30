import numpy as np

def smooth(x, top=0.1):
  n = len(x)
  k = int(top*n)
  X = np.fft.fft(x)
  s = X * np.conj(X) / n
  return np.fft.ifft(X * (s >= np.partition(s, -k)[-k:][0]))
