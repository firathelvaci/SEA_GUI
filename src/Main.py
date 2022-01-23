#! /usr/bin/env python3
import matplotlib.pyplot  as plt
from MainWindow import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 




def main():
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=Ui_MainWindow()
    widget=QtWidgets.QMainWindow()
    mainwindow.show()

            
   
    try:
        sys.exit(app.exec_())
    except:
        print("Closing window")


    
if __name__=="__main__":
    main()

