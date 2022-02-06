from PyQt5.QtWidgets import*
from datetime import datetime
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np
import random
from stopwatch import Stopwatch


class ui_GraphGUI(QMainWindow):
    def __init__(self):
        super(ui_GraphGUI, self).__init__()
        loadUi("/home/frat/catkin_ws/src/SEA_GUI/Qt5/GraphWindow.ui",self)
        self.f = []
        self.t = []
        self.startflag = False
        self.stopwatch = Stopwatch() 
        self.stopwatch.reset()
        self.StartBtn.clicked.connect(self.OnStartClk)
        self.StopBtn.clicked.connect(self.OnStopClk)
        self.ResetBtn.clicked.connect(self.OnResetClk)
        #self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
    def OnStartClk(self):
        self.stopwatch.start()
        self.startflag = True
        self.StartBtn.setStyleSheet("background-color: green")
        self.StopBtn.setStyleSheet("background-color: #efefef")
       # print(self.StopBtn.palette().window().color().name())

    def OnStopClk(self):
        self.stopwatch.stop()
        self.startflag = False
        self.StopBtn.setStyleSheet("background-color: red")
        self.StartBtn.setStyleSheet("background-color: #efefef")

    def OnResetClk(self):
        self.stopwatch.reset()
        self.f.clear()
        self.t.clear()
        self.update_graph()
        if self.startflag:
            self.stopwatch.start()

    def update_values(self,values):
        if (self.startflag):
            self.f.append(values)
            self.t.append(self.stopwatch.duration)
            self.update_graph()

    def update_graph(self):
        self.MplWidget.canvas.axes1.clear()
        self.MplWidget.canvas.axes1.plot(self.t,self.f)
        self.MplWidget.canvas.draw()

