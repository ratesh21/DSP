# -*- coding: utf-8 -*-
"""DSP_LabVI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eRyfy96ZVlEShe7M5ONk5SOZ0OWOgAmP
"""

#Analysis of Difference Equation, Impulse Response, Unit Step Response, and Convolution

#Given difference equation
# y(n) - y(n-1) + 0.9(n-2) = x(n);

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Impulse response of the system
n1 = -20
n2 = 100
N = np.arange(n1, n2+1, 1)
b = [0, 0, 1] #Coefficients for numerator
a = [1, -1, 0.9] #Coefficients for denominator

residue, poles, zeros = signal.residue(b, a)
print("Residue: ",residue)
print("Poles: ",poles)
print("Zeros: ",zeros)

impulse = np.zeros_like(N)
impulse[20] = 1
h = signal.lfilter(b, a, impulse)
print("Signal: ", h)

plt.stem(h, use_line_collection=True)
plt.title('Impulse Response of the System')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()



#Analysis of Difference Equation, Impulse Response, Unit Step Response, and Convolution

#Given difference equation
# y(n) - y(n-1) + 0.9(n-2) = x(n);

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

n1 = -20
n2 = 100
N = n2 - n1 + 1
b = [0, 0, 1] #Coefficients for numerator
a = [1, -1, 0.9] #Coefficients for denominator

residue, poles, zeros = signal.residue(b, a)
print(residue)
print(poles)
print(zeros)

impulse = np.zeros(N)
impulse[0] = 1
sig = signal.lfilter(b, a, impulse)
print("Signal: ", sig)

pulse = np.zeros(N)
pulse[9] = 1
sig_filt = signal.lfilter(b, a, pulse)
convolution = np.convolve(sig, pulse)
print("Convolution: ", convolution)

plt.stem(sig_filt, use_line_collection=True)
plt.title('SIg_filt')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

plt.stem(convolution, use_line_collection=True)
plt.title('Convolution')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

plt.stem(sig, use_line_collection=True)
plt.title('Impulse Response of the System')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()



#Analysis of Difference Equation, Impulse Response, Unit Step Response, and Convolution

#Given difference equation
# y(n) - y(n-1) + 0.9(n-2) = x(n);

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Unit Step Response of the System
n1 = -20
n2 = 100
N = np.arange(n1, n2+1, 1)
b = [0, 0, 1] #Coefficients for numerator
a = [1, -1, 0.9] #Coefficients for denominator

residue, poles, zeros = signal.residue(b, a)
print("Residue: ",residue)
print("Poles: ",poles)
print("Zeros: ",zeros)

unit_step = np.zeros_like(N)
unit_step[20:] = 1
h = signal.lfilter(b, a, unit_step)
print("Signal: ", h)

plt.stem(h, use_line_collection=True)
plt.title('Unit Step Response of the System')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

#Determining the stability of the system by the pole-zero plot

#Analysis of Difference Equation, Impulse Response, Unit Step Response, and Convolution

#Given difference equation
# y(n) - y(n-1) + 0.9(n-2) = x(n);

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


n1 = -20
n2 = 100
N = np.arange(n1, n2+1, 1)
b = [0, 0, 1] #Coefficients for numerator
a = [1, -1, 0.9] #Coefficients for denominator

residue, poles, zeros = signal.residue(b, a)
print("Residue: ",residue)
print("Poles: ",poles)
print("Zeros: ",zeros)

#Unit Step Response of System
unit_step = np.zeros_like(N)
unit_step[20:] = 1
h1 = signal.lfilter(b, a, unit_step)
print("Signal: ", h)

#Impulse Response of System
impulse = np.zeros_like(N)
impulse[20] = 1
h2 = signal.lfilter(b, a, impulse)
print("Signal: ", h)

plt.stem(h1, use_line_collection=True)
plt.title('Unit Step Response of the System')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

plt.stem(h2, use_line_collection=True)
plt.title('Impulse Response of the System')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

z, p, k = signal.tf2zpk(b,a)
print()
print("Zeros: ", z)
print("Poles: ", p)
print("Gain: ", k)

plt.figure()
plt.scatter(np.real(z), np.imag(z), color='r', marker='o', label='Zeros')
plt.scatter(np.real(p), np.imag(p), color='b', marker='x', label='Poles')

unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Pole-Zero Plot of the Difference Equation')
plt.xlabel('Real')
plt.ylabel('Imaginary')

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.grid()

plt.legend()
plt.show()

print("Since the poles lie inside the unit circle, the system is stable")



#Analysis of Difference Equation, Impulse Response, Unit Step Response, and Convolution

#Given difference equation
# y(n) - y(n-1) + 0.9(n-2) = x(n);

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#Input sequence x(n) = (0.8)^n * u(n)
m = np.arange(0, 26, 1)
x = 0.8**(m)
print("Values of x(n): ",x)
print()
print("mth sample: ",m)

#Impulse h(n) = (-0.9)^n * u(n)
h = (-0.9)**(m)
print("Values of h(n): ",h)
print()
print("mth sample: ",m)

plt.stem(x, use_line_collection=True)
plt.title('Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

plt.stem(h, use_line_collection=True)
plt.title('Signal h(n)')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)
plt.show()

#a) Determining y(n) analytically
def tf_coeff():
  #Roots and their multiplicities
  z1 = 0.8
  z2 = -0.9

  mul1 = 1
  mul2 = 1

  poly1 = np.poly([z1] * mul1)
  poly2 = np.poly([z2] * mul2)

  a_coeff = np.polymul(poly1, poly2)

  b_coeff = [1, 0, 0]
  return b_coeff, a_coeff

b, a = tf_coeff()
print("Coefficients of Poles: ", a)
print()

residue, poles, zeros = signal.residuez(b, a)
print("Residue: ",residue)
print("Poles: ",poles)
print("Zeros: ",zeros)

impulse = np.zeros_like(m)
impulse[0] = 1
y_analytical = signal.lfilter(b, a, impulse)
t = np.arange(0,51)
print("Signal outputs found analytically: ", y_analytical)

plt.stem(y_analytical, use_line_collection=True)
plt.title('Analytical')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

#b) By using in-built convolution
y_convolution = np.convolve(x, h)
print("Signal outputs found using inbuilt convolve function: ", y_convolution)

#b) By using user-defined methods
def folding(h):
  return h[::-1]

def padd(x,h):
  l1 = len(x)
  l2 = len(h)

  convolved_length = l1 + l2 - 1
  x_pad = np.zeros(convolved_length)
  h_pad = np.zeros(convolved_length)

  x_pad[:l1] = x
  h_pad[:l2] = h

  return x_pad, h_pad

def multiply(x,h,m,k):
  y = 0
  len_h = len(h)
  y = x[k]*h[len_h-m+k]
  return y

def add(x,h,m):
  y = 0
  for i in range(m):
    y = y + multiply(x,h,m,i)
  return y

conv_length = len(x) + len(h) - 1
x, h = padd(x,h)
h = folding(h)
y_userconv = np.zeros(conv_length)
for i in range(conv_length):
  y_userconv[i] = add(x,h,i)

print("Signal outputs found using user-defined convolution function: ", y_userconv)


plt.stem(y_convolution, use_line_collection=True)
plt.title('Convolution')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

plt.stem(y_userconv, use_line_collection=True)
plt.title('User-defined Convolution')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

#c) by using filter function to calculate y(n) = x(n) * h(n)


z, p, k = signal.tf2zpk(b,a)
print()
print("Zeros: ", z)
print("Poles: ", p)
print("Gain: ", k)

plt.figure()
plt.scatter(np.real(z), np.imag(z), color='r', marker='o', label='Zeros')
plt.scatter(np.real(p), np.imag(p), color='b', marker='x', label='Poles')

unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Pole-Zero Plot of the Difference Equation')
plt.xlabel('Real')
plt.ylabel('Imaginary')

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.grid()

plt.legend()
plt.show()

print("Since the poles lie inside the unit circle, the system is stable")