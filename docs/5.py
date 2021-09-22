# ref: [Embedding in Tk — Matplotlib 3.4.3 documentation](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html)
import tkinter

from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure


fig = Figure()
ax = fig.add_subplot(111) # 添加一个axes到fig
p1 = ax.bar([1,2,3,4,5],[1,4,5,3,1])

ax.set_xlabel('Xrs', size='small')
ax.set_ylabel('Yrs', size='small')
# 设置图形标题
ax.set_title('A graph title', size='small')

# set the edgecolor and facecolor of the axes rectangle to be the same
ax.set_facecolor('grey')

labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_size('x-small')

for r in p1:
    r.set_edgecolor('red')

app = QtWidgets.QApplication([])

# 以下代码是使图片能够即时显示在桌面，如果使有plt.figure()实例化figure类，可以自动
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

toolbar.pack(side=tkinter.TOP, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

root.mainloop() # 与plt.show()作用类似，启动GUI loop使画的图想显示