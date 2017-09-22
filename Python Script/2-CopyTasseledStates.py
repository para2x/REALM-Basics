import arcpy
from arcpy.sa import *
import os
#------------------------------
address=r'E:\APSIMRegion\gSSURGO_Masked'
arcpy.env.overwriteOutput = True
arcpy.env.parallelProcessingFactor="100%"
arcpy.env.workspace=os.path.join(address)
os.chdir(arcpy.env.workspace)
directories = [ x for x in os.listdir('.') if os.path.isdir(x) ] # finding all the folders
for dirr in directories:
    arcpy.env.workspace=os.path.join(address,dirr,"Out")
    fc = arcpy.ListFeatureClasses("*_merged*")
    if len(fc)>0:
        print fc[0]+"\n"
        out_data=os.path.join(address,dirr,fc[0])
        arcpy.Copy_management(fc[0], out_data)
        arcpy.Delete_management (fc[0])
