#!/usr/bin/env python
# -*- coding: utf-8 -*-
#==============================================================================
# main file for creating apsimRegion experiments
#==============================================================================

import os
from apsimRegions.preprocess.configMaker import create_many_config_files
from apsimRegions.preprocess.apsimPreprocess import preprocess_many
from apsimRegions.preprocess.batch import create_run_all_batchfile

def main():
    experimentName = 'CS2'
    outputDir = 'C:/Users/Para2x/Dropbox/PersonalProject/LargeScale-EONR/LargeScale-EONR/{0}'.format(experimentName)

    # validArgs are 'resolution','crop','model','crit_fr_asw', 'sowStart', or 'soilName'
    #factorials = {'soilName':['auto','HCGEN0001','HCGEN0003','HCGEN0007','HCGEN0010','HCGEN0011','HCGEN0013','HCGEN0014','HCGEN0015','HCGEN0016','HCGEN0017','HCGEN0025']}
    #factorials = {'sowStart':['auto']}
    #factorials = {'BAR':['10000','20000']}
    #factorials = {'crit_fr_asw':['0.0','0.95','1.0']}
    factorials = {'NAR':['0.0','60','120','180','240','300']}
    #factorials = {'NAR':['0.0']}
    otherArgs = {'metFileDir':'C:/Users/hamzed/Dropbox/PersonalProject/LargeScale-EONR/PythonScripts/factorial/metfiles/%(met)s',\
                'gridLutPath':'C:/Users/Para2x/Dropbox/PersonalProject/LargeScale-EONR/PythonScripts/factorial/LookUp.csv',\
                'apsimModelDir':'C:/Program Files (x86)/Apsim77-r3632/Model',\
                'soilDataPath':'C:/Program Files (x86)/Apsim77-r3632/UserInterface/ToolBoxes/Carroll.soils',\
                'model':'Carroll',\
                'clockStart':'1/1/2007',\
                'clockEnd':'31/12/2016', \
                'crop':'maize', \
                'density':'8',\
                'depth':'30',\
                'somcrop':'maize',\
                'cnr':'75',
                'mass':'4500',
                'cultivar':'B_105',\
                'row_spacing':'760',\
                'FertDepth':'50',\
                'outputVariables':'mm/dd/yyyy as date, yield, biomass, lai'}

    # create directory if it doesn't exist
    if not os.path.isdir(outputDir):
        os.mkdir(outputDir)

    # create config files
    print 'Creating configuration files...'
    runs = create_many_config_files(outputDir, factorials, otherArgs)

    # create apsim files
    print 'Saving .apsim and .bat files...'
    preprocess_many(outputDir, runs.keys()[0], runs.keys()[-1])

    # create run all batchfile
    create_run_all_batchfile(outputDir, runs, experimentName)

    # feedback
    print 'All files saved to:\r', outputDir
    print '\nFolder', ': Variable'
    for key in runs.keys():
        print '{0:6} : {1}'.format(key, runs[key])

    # save text file of run data
    if not os.path.isfile(os.path.join(outputDir,'readme.txt')):
        mode = 'w'
    else:
        mode = 'a'

    with open(os.path.join(outputDir,'readme.txt'),mode=mode) as f:
        f.write('Folder : Variable')
        for key in runs.keys():
            f.write('\n{0:6} : {1}'.format(key, runs[key]))
        f.write('\n')

    print '\n***** Done! *****'

# Run main() if module is run as a program
if __name__ == '__main__':
    main()
