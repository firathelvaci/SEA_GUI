from PyQt5.QtWidgets import*
from datetime import datetime
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np

class ui_GraphGUI(QMainWindow):
    def __init__(self):
        super(ui_GraphGUI, self).__init__()
        loadUi("/home/frat/catkin_ws/src/SEA_GUI/Qt5/GraphWindow.ui",self)
        
        
        #self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self,name,df1,df2,df3,df4):

        f = df1["Hız"]
        t= df1["Time"]

        self.deneme.canvas.axes1.clear()
        self.deneme.canvas.axes1.plot(t,f)

        f = df2["Hız"]
        t= df2["Time"]

        self.deneme.canvas.axes2.clear()
        self.deneme.canvas.axes2.plot(t,f )

        f = df3["Hız"]
        t= df3["Time"]

        self.deneme.canvas.axes3.clear()
        self.deneme.canvas.axes3.plot(t,f )

        f = df4["Hız"]
        t= df4["Time"]

        self.deneme.canvas.axes4.clear()
        self.deneme.canvas.axes4.plot(t,f )


        self.deneme.canvas.draw()

