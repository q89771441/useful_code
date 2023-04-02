import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
matplotlib.use('Agg')
# 定義二元高斯分佈的參數
mu = np.array([0, 0])
cov = np.array([[1, 0.5], [0.5, 2]])

# 初始化 Gibbs sampling 的參數
num_samples = 5000
x = np.zeros((num_samples, 2))
x[0] = np.random.normal(size=2)

# 定義用於動畫的函數
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_title("Gibbs sampling from a bivariate Gaussian distribution")

scatter = ax.scatter(x[:, 0], x[:, 1], s=2)

def update(frame):
    global x
    x_i = x[frame-1]
    mu_0 = cov[1, 0] / cov[0, 0] * (x_i[0] - mu[0])
    sigma_0 = np.sqrt(cov[1, 1] - cov[1, 0] / cov[0, 0] * cov[0, 1])
    x_i[1] = np.random.normal(loc=mu_0, scale=sigma_0)
    
    mu_1 = cov[0, 1] / cov[1, 1] * (x_i[1] - mu[1])
    sigma_1 = np.sqrt(cov[0, 0] - cov[0, 1] / cov[1, 1] * cov[1, 0])
    x_i[0] = np.random.normal(loc=mu_1, scale=sigma_1)
    
    x[frame] = x_i
    scatter.set_offsets(x[:frame])
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=num_samples, interval=1, blit=True)


#show animation
ani.save('gibbs_sampling.gif', writer='imagemagick', fps=30)