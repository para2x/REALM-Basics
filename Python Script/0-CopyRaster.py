import os,arcpy
arcpy.env.workspace=r'C:\Users\Para2x\Desktop\gSSURGO_Masked'
os.chdir(arcpy.env.workspace)
rasters = arcpy.ListRasters("*")
for raster in rasters:
    name=raster[0:2].upper()
    print name
    if not os.path.exists(name):
        os.mkdir(name)
        #shutil.move(raster, os.path.join(name,raster))
        arcpy.CopyRaster_management(raster,os.path.join(name,raster))
