# import matplotlib.backends as mbackends

# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.figure as mfigure
# import matplotlib

# render = mbackends.backend_agg.RendererAgg(10,20,90)
# fig1=mfigure.Figure()
# canvas=matplotlib.backends.backend_Qt5Agg.FigureCanvas(fig1)
# # canvas=bk(fig1)
# # canvas=matplotlib.backends.backend_tkcairo(fig1)
# ax1=fig1.add_subplot(111)
# ax1.plot([1,2,3,4])
# fig1.draw(render)
# fig1.draw_artist(ax1)
# # canvas.draw()
# plt.show()
# # canvas.print_png("1.png")
# # plt.show()
# # Option 2: Retrieve a view on the renderer buffer...
# # buf = canvas.buffer_rgba()
# # # ... convert to a NumPy array ...
# # X = np.asarray(buf)
# # # ... and pass it to PIL.
# # from PIL import Image
# # im = Image.fromarray(X)

# # # Uncomment this line to display the image using ImageMagick's `display` tool.
# # im.show()

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure

# fig = Figure()
# canvas = FigureCanvas(fig)
# ax = fig.add_subplot(111)
# ax.plot([1,2,3])
# ax.set_title('hi mom')
# ax.grid(True)
# ax.set_xlabel('time')
# ax.set_ylabel('volts')
# canvas.print_figure('test')

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import EllipseSelector

# def onselect(eclick, erelease):
#     "eclick and erelease are matplotlib events at press and release."
#     print('startposition: (%f, %f)' % (eclick.xdata, eclick.ydata))
#     print('endposition  : (%f, %f)' % (erelease.xdata, erelease.ydata))
#     print('used button  : ', eclick.button)

# def toggle_selector(event):
#     print(' Key pressed.')
#     if event.key in ['Q', 'q'] and toggle_selector.ES.active:
#         print('EllipseSelector deactivated.')
#         toggle_selector.RS.set_active(False)
#     if event.key in ['A', 'a'] and not toggle_selector.ES.active:
#         print('EllipseSelector activated.')
#         toggle_selector.ES.set_active(True)

# x = np.arange(100.) / 99
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)

# toggle_selector.ES = EllipseSelector(ax, onselect, drawtype='line')
# fig.canvas.mpl_connect('key_press_event', toggle_selector)
# plt.show()


# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from matplotlib.lines import Line2D
# import matplotlib.pyplot as plt
# import matplotlib

# def show(fig):
#     dummy = plt.figure()
#     new_manager = dummy.canvas.manager
#     new_manager.canvas.figure = fig
#     fig.set_canvas(new_manager.canvas)

# fig = Figure()
# # 可以使用figsize关键字设置figure的大小
# # fig = Figure(figsize=(2.04,1.92))
# # canvas = FigureCanvas(fig) # canvas需要与figure关联
# # manger = matplotlib.backend_bases.FigureManagerBase(canvas,1)
# # manger.canvas=FigureCanvas(fig)



# ax = fig.add_subplot(111) # 添加一个axes到fig 
# # ax = fig.add_axes([0.2,0.2,0.5,0.7]) # 添加一个axes到fig并指定axes的位置及长宽，使用set_position()方法可以修改已有axes的位置大小

# p1 = ax.bar([1,2,3,4,5],[1,4,5,3,1])

# ax.set_xlabel('Xrs', size='small')
# ax.set_ylabel('Yrs', size='small')
# # 设置图形标题
# ax.set_title('A graph title', size='small')

# # set the edgecolor and facecolor of the axes rectangle to be the same
# ax.set_facecolor('grey')

# labels = ax.get_xticklabels() + ax.get_yticklabels()
# for label in labels:
# 	label.set_size('x-small')

# for r in p1:
# 	r.set_edgecolor('red')
# fig.canvas.draw()
# # print(plt.getp(fig.canvas))
# show(fig)
# # fig.canvas.manager.show()
# # fig.savefig("aa.png")
# # canvas.print_figure("nn")


# fig = Figure()
# canvas = FigureCanvas(fig)
# manger = matplotlib.backend_bases.FigureManagerBase(canvas,1)


# manger.show()



# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvasTkAgg
# from matplotlib.backends.backend_tkcairo import FigureCanvasTkCairo as FigureCanvasTkCairo
# from matplotlib.figure import Figure
# from matplotlib.lines import Line2D
# import matplotlib.pyplot as plt
# import matplotlib
# import tkinter


# def show(fig):
#     dummy = plt.figure()
#     new_manager = dummy.canvas.manager
#     new_manager.canvas.figure = fig
#     fig.set_canvas(new_manager.canvas)
#     print(matplotlib.get_backend())

# # matplotlib.use('Agg')
# print(matplotlib.get_backend())
# fig = Figure()
# # canvas = FigureCanvas(fig) # canvas需要与figure关联
# # manger = matplotlib.backend_bases.FigureManagerBase(canvas,1)
# root = tkinter.Tk()

# ax = fig.add_subplot(111) # 添加一个axes到fig 

# p1 = ax.bar([1,2,3,4,5],[1,4,5,3,1])

# ax.set_xlabel('Xrs', size='small')
# ax.set_ylabel('Yrs', size='small')
# # 设置图形标题
# ax.set_title('A graph title', size='small')

# # set the edgecolor and facecolor of the axes rectangle to be the same
# ax.set_facecolor('grey')

# labels = ax.get_xticklabels() + ax.get_yticklabels()
# for label in labels:
#     label.set_size('x-small')

# for r in p1:
#     r.set_edgecolor('red')

# # show(fig)
# # fig.show()
# # ff=plt.figure()
# # canvas1=ff.canvas
# # # manger1=ff.canvas.manager
# # manger1.canvas.figure=fig
# # fig.set_canvas(manger1.canvas)
# # plt.show()
# print(len(dir(fig.canvas)))

# canvas = FigureCanvasTkAgg(fig,master=root)
# # canvas = FigureCanvasTkCairo(fig)
# mm = plt.new_figure_manager(1)
# canvas.manager=mm
# manger = matplotlib.backend_bases.FigureManagerBase(canvas,1)
# fig.set_canvas(canvas)
# # fig.show()
# print(len(dir(canvas)))
# canvas.draw()
# print(len(dir(canvas)))

# print(canvas.renderer)
# canvas.get_renderer

# ff=plt.figure()
# cc=ff.canvas
# print(cc)
# print(canvas)
# for i in dir(cc):
# 	if i not in dir(canvas):
# 		print(i)
# # print(matplotlib.get_backend())
# plt.show()



import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
