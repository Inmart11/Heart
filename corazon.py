import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def heart_points(t):
    return (16 * np.sin(t) ** 3, 
            13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))

fig, ax = plt.subplots()
ax.set_xlim(-16, 16)
ax.set_ylim(-16, 16)
ax.set_aspect("equal", "box")
ax.axis("off")
fig.patch.set_facecolor("black")

heart, = ax.plot([], [], color="purple", lw=2)

def init():
    heart.set_data([], [])
    return heart,

def animate(i):
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = heart_points(t)
    scale = 1 + 0.5 * np.sin(np.pi * i / 25)
    heart.set_data(x * scale, y * scale)
    heart.set_linewidth(3 + 1 * np.sin(np.pi * i / 25))
    heart.set_color((0.6 + 0.4 * np.sin(np.pi * i / 25), 0, 0))
    return heart,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.show()
