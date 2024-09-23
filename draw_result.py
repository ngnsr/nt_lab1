import matplotlib.pyplot as plt
import numpy as np

x1 = [0.7, 0.8869914163090128, 0.9589798362358462, 0.9854802590891854, 0.9949168629592726,
      0.9982278788917373, 0.9993831126302712, 0.9997853701051378, 0.999925338810917, 0.9999740300057041]
f1 = [-4.3568999999999996, -1.663868967695251, -0.6105967773120646, -0.21717890605527934, -0.07617019679441484,
      -0.026572423200374118, -0.00925217006948742, -0.0032193102743907076, -0.001119901115444577, -0.00038954789120282385]

x2 = [0.7, 0.9562882352941176, 0.994544604057781, 0.9993529844114568, 0.9999238067229128,
      0.9999910350606935, 0.9999989452870753]
f2 = [-4.3568999999999996, -0.6503582689822789, -0.08174246601248925, -0.009703979294751974,
      -0.0011428817422718396, -0.00013447384849030186, -1.5820690531853643e-05]

plt.scatter(x1, f1, color='blue', label='iteration', s=50)

plt.scatter(x2, f2, color='red', label='relaxation', s=50)

for i in range(len(x1)):
    plt.annotate(f'{i}', (x1[i], f1[i]), textcoords="offset points", xytext=(
        5, -5), ha='center', fontsize=8, color='blue')

for i in range(len(x2)):
    plt.annotate(f'{i}', (x2[i], f2[i]), textcoords="offset points", xytext=(
        5, -5), ha='center', fontsize=8, color='red')

plt.xlim(0.7, 1.00005)
plt.ylim(-4.5, 0.1)

plt.xticks(np.arange(0.7, 1.0001, 0.05))

plt.yticks(np.arange(-4.5, 0.2, 0.5))

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Точки для x і f(x) з номерами')
plt.grid(True)

plt.show()
