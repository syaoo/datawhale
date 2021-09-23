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



# import tkinter

# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure
# import matplotlib
import matplotlib.pyplot as plt
# import numpy as np

# def set_size(w,h, ax=None):
#     """ w, h: width, height in inches """
#     if not ax: ax=plt.gca()
#     l = ax.figure.subplotpars.left
#     r = ax.figure.subplotpars.right
#     t = ax.figure.subplotpars.top
#     b = ax.figure.subplotpars.bottom
#     figw = float(w)/(r-l)
#     figh = float(h)/(t-b)
#     ax.figure.set_size_inches(figw, figh)

# x = np.arange(0,2*np.pi,0.1)
# y = np.sin(x)

# fig=plt.figure(figsize=(10,11))
# ax1 = plt.subplot(3,2,1)
# ax1.plot(x,y)
# ax1.set_title("3,2,1")
# ax2 = plt.subplot(322)
# ax2.plot(x,y)
# ax2.set_title("322")
# ax3 = plt.subplot(3,2,(3,4))
# ax3.plot(x,y)
# ax3.set_title("3,2,(3,4)")
# ax4 = plt.subplot(3,2,(5,6))
# ax4.plot(x,y)
# ax4.set_title("3,2,(5,6)")
# plt.delaxes(ax1)
# plt.axes(ax1)
# plt.show()

"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 下面三种写法等价
ax1 = plt.subplot(221)
ax1 = plt.subplot(2, 2, 1)
spec = gridspec.GridSpec(ncols=2, nrows=2)
ax1 = plt.subplot(spec[0,0])

# 添加一个没有边框的axes
ax2 = plt.subplot(222, frameon=False)
ax2.plot([1,2,3, 6])
# 添加一个极坐标的axes
plt.subplot(223, projection='polar')

# 添加一个红色背景、与ax2共享x轴的axes
plt.subplot(224, sharex=ax2, facecolor='red')
plt.show()
"""


import matplotlib.pyplot as plt
import numpy as np
"""
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# Create four polar axes and access them through the returned array
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

# Create figure number 10 with a single subplot
# and clears it if it already exists.
fig, ax = plt.subplots(num=10, clear=True)
plt.show()
"""
from matplotlib.figure import Figure

fg = Figure(constrained_layout=False,tight_layout=True)
ax = fg.subplots(3, 1)

for i in range(3):
    ax[i].plot(range(5+5*i))

fg.suptitle('lots of lines')

fg.savefig("example2.png")