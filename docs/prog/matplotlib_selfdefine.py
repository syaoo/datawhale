import sys
from matplotlib.figure import Figure
# ref: [Embedding in Tk — Matplotlib 3.4.3 documentation](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html)

def showQt(fig:Figure):
	"""
	在Qt界面中显示图像
	"""
	"""
	PySide6暂不支持，matplotlib 3.5应该会支持、使用方法类似

    使用PySide2/6如出现下面错误：
    ```
    qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
    ```
    可增加以下代码解决：
    ```
    dirname = os.path.dirname(PySide6.__file__)
    pluging_path = os.path.join(dirname,'plugins','platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=pluging_path
    ```
    ref: https://blog.csdn.net/weixin_40922744/article/details/111355088
	"""

	from PySide2 import QtCore, QtWidgets, QtGui
	from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

    # 初始化qt应用程序
	if not QtWidgets.QApplication.instance():
	    app = QtWidgets.QApplication(sys.argv)
	else:
	    app = QtWidgets.QApplication.instance()

	mw = QtWidgets.QMainWindow()  #初始化主窗口
	mw.setWindowTitle("Figure 1") #设置标题
	window = QtWidgets.QWidget()  #初始化窗户组件
	layout = QtWidgets.QVBoxLayout() #初始化窗户布局
	canvas = FigureCanvas(fig) # 生成一个qt绘图区域
	canvas.draw()
	layout.addWidget(canvas)
	layout.setMargin(0)
	window.setLayout(layout)

	mw.addToolBar(NavigationToolbar(canvas,window)) # 增加工具栏
	# mw.addToolBar(QtCore.Qt.BottomToolBarArea,NavigationToolbar(canvas,window)) # 在底部增加工具栏
	mw.setCentralWidget(window)
	mw.show()

	app.exec_()

def showTk(fig:Figure):
    """
    在Tk界面中显示图像
    """
    import tkinter
    from matplotlib.backends.backend_tkagg import (
        FigureCanvas, NavigationToolbar2Tk as NavigationToolbar)

    root = tkinter.Tk() # 生成Tkinter窗口
    root.wm_title("Figure 1")

    canvas = FigureCanvas(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()

    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar(canvas, root, pack_toolbar=False) # 生成Tk工具栏
    toolbar.update()

    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    root.mainloop() # 与plt.show()作用类似，启动GUI loop使画的图想显示

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

fig.savefig("savedpic.png") #直接保存图像


showTk(fig) # 使用Tk后端显示图像
showQt(fig) # 使用Qt后端显示图像

