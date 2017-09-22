from multiprocessing import Pool, TimeoutError
import arcpy
from arcpy import env
from arcpy.sa import *
import os
#
arcpy.CheckOutExtension("Spatial")
def RastoPolyDis(dirR):
    address=r'C:\Users\Para2x\Desktop\gSSURGO_Masked'
    arcpy.env.overwriteOutput = True
    arcpy.env.parallelProcessingFactor="100%"
    arcpy.env.workspace=os.path.join(address,dirR)
    rasters = arcpy.ListRasters("*")
    for raster in rasters:
        name=raster[0:2].upper()
        try:
            memoryFeature = name+"_Poly.shp"
            arcpy.RasterToPolygon_conversion(raster, memoryFeature, "SIMPLIFY", "VALUE")
            print name
            arcpy.Dissolve_management (memoryFeature, name+"_dissolved.shp","GRIDCODE")
        except Exception as e:
            print "Error processing", raster
            print "Error", e

#############################################
if __name__ == '__main__':
    address=r'C:\Users\Para2x\Desktop\gSSURGO_Masked'
    pool = Pool(2)               # start 4 worker processes
    #####################
    os.chdir(address)
    directories = [ x for x in os.listdir('.') if os.path.isdir(x) ] # finding all the folders
    #del directories[0]## removing the just soil folder
    #print directories[0]
    ######################
    pool.map(RastoPolyDis, directories)
    pool.close()
    pool.join()
