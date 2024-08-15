import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')

x_train = np.array([1,2])
y_train = np.array([300,500])

m=len(x_train)
print("Number of training examples is " + m)

i=0
x_i=x_train[i]
y_i=y_train[i]
print("(x^(" + i + "), y^(" + i + ")) = (" + x_i + "," + y_i + ")" )