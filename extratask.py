import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], animated=True)


def init():  # Инициализируем график
    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    return ln,


def update(frame):  # Прорисовываем каждое новое значение графика
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(-2*np.pi, 2*np.pi, 32),
                    init_func=init, blit=True)  # Указываем параметры для анимации графика

writer = PillowWriter(fps=24)
ani.save('animated_plot.gif', writer=writer)  # Сохраняем .gif файл с анимацией
plt.show()
