"""
Created on Thu Apr 21 19:05:15 2022

@author: javier
"""

import os

model_path = os.path.dirname(os.path.abspath('Model_Phase_B_Pillars.sysmdl'))
print(model_path)
with open('Meshing_Phase_B_Pillars.sysmsh', 'r', encoding='utf-8') as file:
    data = file.readlines()
data[569] ='                ' + ' <ELEM FILE_PATH=" ' + model_path + '\Model_Phase_B_Pillars.sysmdl' + '" TYPE="FILE_DESCRIPTION" FILE_FORMAT="sysmdl" NAME="MODEL" FILE_RELATIVE_PATH="./model_V2.1.sysmdl"/> \n'

with open('Meshing_Phase_B_Pillars.sysmsh', 'w', encoding='utf-8') as file:
    file.writelines(data) 
