# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:01:21 2018

@author: Mathu_Gopalan
"""
import os, pandas as pd
folder = 'D:\\Infy\\AEM project\\OH Portal\\McCann\\MRM Finals\\GEP_R2S1_Sensitivity_Delivery_110618\\R2 S1 - Sensitivity\\Images'
folder_size = 0
df= pd.DataFrame(columns =["name","filesize"])
detail = {"name":"filename","size":"filesize"}
for (path, dirs, files) in os.walk(folder):
  for file in files:
    filename = os.path.join(path, file)
    fol_size = os.path.getsize(filename)
   # df =df.append(pd.DataFrame(filename, fol_size)
    df = df.append(pd.DataFrame({'name':filename,'filesize':fol_size},index=[0]),ignore_index=True)
    
    #detail.update ({"name":filename,"size":fol_size})
    #detail["name"] = filename
    #detail["size"] = fol_size
    
    