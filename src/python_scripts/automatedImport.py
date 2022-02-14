# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 8.0.26



'''
data = ['0:UFAL', '1:NetType', '2:Year', '3:Month', '4:Day', '5:Hour',
        '6:Minute', '7:Second', ':Nanosecond', ':Latitude', ':Longitude', ':Altitude',
        ':AltUncertinty', ':PeakCurrent', ':VFR', ':Multiplicity', ':PulseCount', ':SensorCount',
        ':DegreeOfFreedom', ':EllipseAngle', ':Error1', ':Error2', ':ChiSquard', ':RiseTime',
        ':PeakToZero', ':RateOfRise', ':CloudIndicator', ':AngleIndicator', ':Signal Indicator', ':TimingIndicator']

'''
import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
import mysql.connector
from datetime import datetime

# sample time of how the data base wants the format
now = datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')

# reads the ASCII file than convers to 2D list
df = pd.read_csv('~/Downloads/00.txt', sep='	')
df_list = df.values.tolist()

# connects to the data base
mydb = mysql.connector.connect(
    host='97.102.250.88',
    user='root',
    password='Sadie1289',
    database='Lightning_Data'
)

mycursor = mydb.cursor()

# pushes evver row in the ASCII file to the data base
for row in df_list:
    sampleTime = str('%s-%s-%d %s:%s:%s.%s' % (int(row[2]), int(row[3]), int(
        row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8])))

    mycursor.execute(f"INSERT INTO Lightning_Data.lightning_record VALUES ('{sampleTime}',{row[9]},{row[10]},{row[23]},{row[24]},{row[13]})")

    mydb.commit()


