import torch
import torch.nn.functional as tnf
import matplotlib.pyplot as plt

x = torch.linspace(-5, 5, 200)
x_np = x.data.numpy()

y_relu = tnf.relu(x).data.numpy()
y_sigmoid = tnf.sigmoid(x).data.numpy()
y_tanh = tnf.tanh(x).data.numpy()
y_softplus = tnf.softplus(x).data.numpy()

plt.figure(1, figsize=(8, 6))
plt.subplot(221)
plt.plot(x_np, y_sigmoid, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')
plt.show()