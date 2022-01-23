from array import array
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
import threading
from re import S
import rospy
import numpy as np
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension,Float32MultiArray
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats



class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        loadUi("/home/frat/catkin_ws/src/SEA_GUI/Qt5/Mainwindow.ui",self)
        self.z_motor_sub_msg = Float32MultiArray()
        self.z_motor_pub_msg = Float32MultiArray()
        self.z_motor_pub_msg.data = np.zeros(4)
        self.z_motor_sub_msg.data = np.zeros(4)
        rospy.init_node('master_device')
        self.rate=rospy.Rate(2)
        self.z_motor_pub=rospy.Publisher('z_motor_pub',Float32MultiArray,queue_size=10)
        self.z_motor_sub = rospy.Subscriber('z_motor_sub',Float32MultiArray, self.z_motor_callback)

        self.StartBtn.clicked.connect(self.OnStartClk)
        self.StopBtn.clicked.connect(self.OnStopClk)
        self.ZSetBtn.clicked.connect(self.ZSetClk)
        self.ManualRb.setChecked(True)
        x = threading.Thread(target=self.thread_function, args=(1,))
        x.start()

    
    def z_motor_callback(self,msg1):
        self.z_motor_sub_msg.data = msg1.data
        print(self.z_motor_sub_msg.data )

    def ZSetClk(self):
        self.z_motor_pub_msg.data[2]=self.ZVelSetSB.value()

    def OnStartClk(self):
        self.z_motor_pub_msg.data[0] = 1
        if self.ManualRb.isChecked() == True:
            self.z_motor_pub_msg.data[1] = 1
        elif self.RefConRb.isChecked() == True:
            self.z_motor_pub_msg.data[1] = 2
        elif self.ExtConRb.isChecked() == True:
            self.z_motor_pub_msg.data[1] = 3
        else:
            self.z_motor_pub_msg.data[1] = 0
        

    def OnStopClk(self):
        self.z_motor_pub_msg.data[0] = 0
        self.z_motor_pub_msg.data[1] = 0
    
    def thread_function(self,name):
        
        while not rospy.is_shutdown():
           
            self.z_motor_pub.publish(self.z_motor_pub_msg)
            self.rate.sleep()
            self.ZVelRefLbl.setText(str(round(self.z_motor_sub_msg.data[0],3)))
            self.ZVelAcLbl.setText(str(round(self.z_motor_sub_msg.data[1],3)))
            self.ZTrqRefLbl.setText(str(round(self.z_motor_sub_msg.data[2],3)))
            self.ZTrqAcLbl.setText(str(round(self.z_motor_sub_msg.data[3],3)))

        
