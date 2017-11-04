import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot2d():
    mpl.rcParams['xtick.labelsize']=24
    mpl.rcParams['ytick.labelsize']=24
    np.random.seed(42)
    x=np.linspace(0,5,100)
    y=2*np.sin(x)+0.3*x**2
    y_data=y+np.random.normal(scale=0.3,size=100)
    plt.figure('data')
    plt.plot(x,y_data,'.')
    plt.figure('model')
    plt.plot(x,y)
    plt.figure('data & model')
    plt.plot(x,y,'k',lw=3)
    plt.scatter(x,y_data)
    plt.savefig('result.png')
    plt.show()

def plot3d():
    np.random.seed(42)
    dim=3
    n_samples=500
    samples=np.random.multivariate_normal(np.zeros(dim),np.eye(dim),n_samples)
    for i in range(samples.shape[0]):
        r = np.power(np.random.random(), 1.0/3.0)
        samples[i] *= r / np.linalg.norm(samples[i])
    upper_samples = []
    lower_samples = []

    for x, y, z in samples:
        # 3x+2y-z=1作为判别平面
        if z > 3*x + 2*y - 1:
            upper_samples.append((x, y, z))
        else:
            lower_samples.append((x, y, z))

    fig = plt.figure('3D scatter plot')
    ax = fig.add_subplot(111, projection='3d')

    uppers = np.array(upper_samples)
    lowers = np.array(lower_samples)

    # 用不同颜色不同形状的图标表示平面上下的样本
    # 判别平面上半部分为红色圆点，下半部分为绿色三角
    ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c='r', marker='o')
    ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')

    plt.show()


if __name__=="__main__":
    plot3d()