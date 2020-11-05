import numpy as np

def denoise(x, top=1/8):
  n = len(x)
  k = int(top*n)
  X = np.fft.fft(x)
  s = X * np.conj(X) / n
  return np.fft.ifft(X * (s >= np.partition(s, -k)[-k:][0]))
