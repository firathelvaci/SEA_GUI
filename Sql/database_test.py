#! /usr/bin/env python3
from ast import While
import sqlite3
import datetime
import os.path

sqliteConnection = sqlite3.connect('/home/frat/catkin_ws/src/SEA_GUI/Sql/Sea.db')

cursor = sqliteConnection.cursor()




def write_to_db(motor_data):
        sqlite_insert_with_param = """INSERT INTO Z_motor
                          (Date, Time, Second, Motor_Run_State, Motor_Control_State, 
                           Motor_Vel_Ref, Motor_Vel_Ac, Motor_Trq_Ref, Motor_Trq_Ac) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(sqlite_insert_with_param, motor_data)
        sqliteConnection.commit()


now = datetime.datetime.now()
date = now.year*10000 + now.month*100 + now.day
time = now.hour*100 + now.minute
second = now.second * 1000000 +  now.microsecond

motor_data=[date,time,second,'Running','Automatic',10.5,20.2,-2.3,-5.7]
write_to_db(motor_data)